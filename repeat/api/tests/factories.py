import factory
import faker
import json

from .. import models
from pdfutil import test_pdfutil

fake = faker.Faker()


def generic_factory(model):
    meta = type("Meta", (), {"model": model})
    return type(model.__name__ + "Factory", (factory.DjangoModelFactory, ),
                {"Meta": meta})


Domain = generic_factory(models.Domain)

class Domain(factory.DjangoModelFactory):
    class Meta:
        model = models.Domain

    name = factory.Faker("sentence", nb_words=2)
    description = factory.Faker("paragraph")


def stub(arg):
    """ Return a constant function of no arguments wrapping a value """

    def inner():
        return arg

    return inner

class Paper(factory.DjangoModelFactory):
    class Meta:
        model = models.Paper

    title = factory.Faker("sentence", nb_words=4)
    unique_id = "isbn10:{}".format(faker.Faker().isbn10())
    authors = factory.LazyFunction(stub(json.dumps([10 * fake.name()])))
    # TODO: when not specifying document_text, we get a traceback.
    document = factory.django.FileField(data=test_pdfutil.BLANK)
    document_text = "text"
