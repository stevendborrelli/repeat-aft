from django.db import models
import polymorphic.models as polymodels
import json


def json_str(cls):
    """
    A class decorator that replaces the __str__ method of a Model with one that
    represents the model as a JSON string.
    """

    def __str__(self):
        dic = {}
        for name, attribute in self.__dict__.items():
            if name != "_state":
                dic[name] = attribute
        return json.dumps(dic)

    cls.__str__ = __str__
    return cls


@json_str
class Domain(models.Model):
    """
    A domain is some scientific subfield. A domain contains many
    variables, though each ``Variable`` can also belong to several domains.
    """
    NAME_HELP = (
        "A unique name of this Domain, used as a primary key (if you don't"
        " know what this means, just make sure it's unique :). Some examples"
        "are 'ehr' or 'nuclear physics'.")
    DESCRIPTION_HELP = "The human-readable description of this domain"

    name = models.TextField(unique=True, primary_key=True, help_text=NAME_HELP)
    description = models.TextField(
        max_length=100000, blank=True, help_text=DESCRIPTION_HELP)


@json_str
class Paper(models.Model):
    """
    An individual paper or study, belonging to one or several domains. A paper
    should have Values corresponding to every Variable in its Domain(s).
    """
    UNIQUE_ID_HELP = (
        "A unique identifier for the paper, prefixed with doi:, isbn:, or pmid"
    )
    TITLE_HELP = (
        "Title of the paper (used in combination with ``authors`` to identify"
        " the paper in absence of a ``unique_id``)")
    AUTHORS_HELP = "Authors of the paper"
    DOCUMENT_HELP = (
        "The Django ``File`` field storing the raw document, usually in PDF"
        " format")

    domains = models.ManyToManyField(Domain)
    unique_id = models.TextField(unique=True, help_text=UNIQUE_ID_HELP)
    title = models.TextField(max_length=1000, help_text=TITLE_HELP)
    authors = models.TextField(max_length=10000, help_text=AUTHORS_HELP)
    document = models.TextField(max_length=10000, help_text=DOCUMENT_HELP)

    class Meta:
        unique_together = [("title", "authors"), ]


@json_str
class Category(models.Model):
    """ A category of variables such as "Methodology", or "Data Collection" """
    NAME_HELP = "A unique identifier for this category"
    DESCRIPTION_HELP = "The human-readable description of this category"
    ORDER_HELP = (
        "Order to present this category to the user (lower is sooner)."
        " For instance, we might want to present all questions relating to "
        " the bibliographic information first. To this end, we would construct "
        " a 'Bibliographic Information' category, and set it's order to 0. ")

    name = models.TextField(unique=True, primary_key=True, help_text=NAME_HELP)
    description = models.TextField(
        max_length=100000, blank=True, help_text=DESCRIPTION_HELP)
    order = models.IntegerField(unique=True)


@json_str
class Variable(polymodels.PolymorphicModel):
    """ A single variable, belonging to one or several Domains. """
    NAME_HELP = "A unique identifier for the variable (used as a primary key)"
    LABEL_HELP = (
        "The human readable description of the variable, usually presented to"
        " the user as a question, e.g. 'Did the author(s) specify which"
        " version of R they used?'")
    IDENTIFIER_HELP = (
        "Could this variable be used to identify any authors or subjects?"
        " Examples of identifiers include institution name and date of birth.")
    CATEGORY_HELP = "The general category, used to group variables in queries"
    ORDER_HELP = (
        "Order to present this variable to the user (lower is sooner)."
        " Category order takes precendence, but this variable determines when"
        " the variables are presented within a category. If we wanted the "
        " ask what the title is of the paper, we would make a Variable named "
        " 'Title' and set its order to 0 (within its category).")
    SKIP_LOGIC_HELP = (
        "A JSON field representing when to ask for the value of this variable."
        " See :ref:`_branching_logic` for more details.")

    domains = models.ManyToManyField(Domain)
    name = models.TextField(
        unique=True, primary_key=True, max_length=10000, help_text=NAME_HELP)
    label = models.TextField(max_length=100000, help_text=LABEL_HELP)
    identifier = models.BooleanField(
        blank=True, default=False, help_text=IDENTIFIER_HELP)
    category = models.ForeignKey(Category, help_text=CATEGORY_HELP)
    order = models.IntegerField(unique=True)
    # TODO JSON field
    skip_logic = models.TextField(
        blank=True, default="", max_length=100000, help_text=SKIP_LOGIC_HELP)


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
    USER_ENTERED_HELP = (
        "Did a user manually enter this field, or was it automatically"
        " extracted?")

    # Set up polymorphic reference to a subclass of Variable
    # https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # variable = GenericForeignKey()

    variable = models.ForeignKey(Variable)
    paper = models.ForeignKey(Paper)
    value = models.TextField(max_length=100000)  # TODO: JSON field
    user_entered = models.BooleanField(default=False)
