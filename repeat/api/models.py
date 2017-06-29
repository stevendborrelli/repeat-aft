from . import util
from django.db import models
from rest_framework import serializers  # for __str__ methods
import django.core.files
import functools
import io
import json
import polymorphic.models as polymodels
import subprocess # exceptions


def get_serializer(cls, fields="__all__", exclude=None):
    """ Create Serializers for a Model on the fly """

    meta = type("Meta", (), {"model": cls, "fields": fields})
    if exclude is not None:
        del meta.fields
        meta.exclude = exclude
    serializer = type(cls.__name__ + "Serializer",
                      (serializers.ModelSerializer, ), {"Meta": meta})
    serializer.__doc__ = ("Serialize the fields " + str(fields) +
                          " from the model " + cls.__name__)
    return serializer


def json_str(cls=None, *, fields="__all__", exclude=None):
    """
    A class decorator that replaces the __str__ method of a Model with one that
    represents the model as a JSON string.

    See: http://dabeaz.com/py3meta/Py3Meta.pdf
    """
    if cls is None:
        return functools.partial(json_str, fields=fields, exclude=exclude)

    cls.serializer = get_serializer(cls, fields=fields, exclude=exclude)
    cls.__str__ = lambda self: json.dumps(cls.serializer(self).data)
    return cls


@json_str
class Domain(models.Model):
    """
    A domain is some scientific subfield. A domain contains many
    variables, though each ``Variable`` can also belong to several domains.
    """

    name = models.TextField(**{
        "unique": True,
        "primary_key": True,
        "help_text":
        ("A unique name of this Domain, used as a primary key (if you don't"
         " know what this means, just make sure it's unique :). Some examples"
         "are 'ehr' or 'nuclear physics'.")
    })
    description = models.TextField(**{
        "max_length": 100000,
        "blank": True,
        "help_text": "The human-readable description of this domain"
    })


@json_str(exclude=("document", "document_text"))
class Paper(models.Model):
    """
    An individual paper or study, belonging to one or several domains. A paper
    should have Values corresponding to every Variable in its Domain(s).
    """
    domains = models.ManyToManyField(Domain)
    unique_id = models.TextField(**{
        "primary_key": True,
        "unique": True,
        "help_text":
        "A unique identifier for the paper, prefixed with doi:, isbn:, or pmid:"
    })
    title = models.TextField(**{
        "max_length": 1000,
        "help_text":
        ("Title of the paper (used in combination with ``authors`` to identify"
         " the paper in absence of a ``unique_id``)")
    })
    authors = models.TextField(**{
        "max_length": 10000,
        "help_text": "Authors of the paper"
    }) # TODO: JSONField
    document = models.FileField(**{
        "upload_to": "pdf/%Y/%m/%d/",
        "help_text":
        ("The Django ``File`` field storing the raw document, usually in PDF"
         " format")
    })
    document_text = models.FileField(**{
        "upload_to": "txt/%Y/%m/%d/",
        "blank": True,
        "help_text":
        "Body of paper, will be extracted automatically if not offered"
    })

    def save(self, *args, **kwargs):
        """ Extract the paper's text before saving """
        text = util.pdf_to_text(self.document.read())
        self.document_text = django.core.files.File(text)
        super(self.__class__, self).save(*args, **kwargs) # save file to disk

    class Meta:
        unique_together = [("title", "authors"), ]


@json_str
class Category(models.Model):
    """ A category of variables such as "Methodology", or "Data Collection" """

    name = models.TextField(**{
        "unique": True,
        "primary_key": True,
        "help_text": "A unique identifier for this category"
    })
    description = models.TextField(**{
        "max_length": 100000,
        "blank": True,
        "help_text": "The human-readable description of this category"
    })
    order = models.IntegerField(**{
        "unique": True,
        "help_text":
        ("Order to present this category to the user (lower is sooner)."
         " For instance, we might want to present all questions relating to "
         " the bibliographic information first. To this end, we would construct "
         " a 'Bibliographic Information' category, and set it's order to 0. ")
    })

    class Meta:
        verbose_name_plural = "Categories"


@json_str
class Variable(polymodels.PolymorphicModel):
    """ A single variable, belonging to one or several Domains. """

    domains = models.ManyToManyField(Domain)
    name = models.TextField(**{
        "unique": True,
        "primary_key": True,
        "max_length": 10000,
        "help_text":
        "A unique identifier for the variable (used as a primary key)"
    })
    label = models.TextField(**{
        "max_length": 100000,
        "help_text":
        ("The human readable description of the variable, usually presented to"
         " the user as a question, e.g. 'Did the author(s) specify which"
         " version of R they used?'")
    })
    identifier = models.BooleanField(**{
        "blank": True,
        "default": False,
        "help_text":
        ("Could this variable be used to identify any authors or subjects?"
         " Examples of identifiers include institution name and date of birth."
         )
    })
    category = models.ForeignKey(Category, **{
        "help_text": "The general category, used to group variables in queries"
    })
    order = models.IntegerField(**{
        "unique": True,
        "help_text":
        ("Order to present this variable to the user (lower is sooner)."
         " Category order takes precendence, but this variable determines when"
         " the variables are presented within a category. If we wanted the "
         " ask what the title is of the paper, we would make a Variable named "
         " 'Title' and set its order to 0 (within its category).")
    })
    # TODO JSON field
    skip_logic = models.TextField(**{
        "blank": True,
        "default": "",
        "max_length": 100000,
        "help_text":
        ("A JSON field representing when to ask for the value of this variable."
         " See :ref:`_branching_logic` for more details.")
    })


@json_str
class Binary(Variable):
    """ A Variable with two choices """
    yes_text = models.TextField(blank=True, default="Yes", max_length=1000)
    no_text = models.TextField(blank=True, default="No", max_length=1000)

    class Meta:
        verbose_name_plural = "Binaries"


@json_str
class OneFromMany(Variable):
    """ A selection of one choice from several options (radio button) """
    options = models.TextField()  # TODO: JSONField

    class Meta:
        verbose_name_plural = "One From Many (Radios)"


@json_str
class ManyFromMany(Variable):
    """ A selection of many choices from many options (checkboxes) """
    options = models.TextField()  # TODO: JSONField

    class Meta:
        verbose_name_plural = "Many From Many (Checkboxes)"


@json_str
class Value(models.Model):
    """ The value of a specific Variable for a specific Paper """
    # Set up polymorphic reference to a subclass of Variable
    # https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField(**{}
    # variable = GenericForeignKey()

    variable = models.ForeignKey(Variable)
    paper = models.ForeignKey(Paper)
    value = models.TextField(max_length=100000)  # TODO: JSON field
    user_entered = models.BooleanField(**{
        "default": False,
        "blank": True,
        "help_text":
        ("Did a user manually enter this field, or was it automatically"
         " extracted?")
    })