"""\
Testing views is really more like integration testing than unit testing, but it
shouldn't matter too much.\
"""

import doctest
import django.core.files.uploadedfile
import django.test
import factory
import json

from . import factories
from pdfutil import test_pdfutil

from .. import views
from .. import models

BASE_URL = "/api/v0"


class ViewTests(django.test.TestCase):
    fixtures = ["fixture.json"]

    def test_extract(self):
        """ Test that variables are extracted properly """
        dom = factories.Domain.create()

        for document in [test_pdfutil.BLANK, test_pdfutil.LOREM]:
            paper = factories.Paper.create(document=factory.django.FileField(
                data=document))
            c = django.test.Client()
            variables = ["funding", "grant_id"]
            for var in variables:
                url = "{}/extract/{}/{}".format(BASE_URL, paper.unique_id, var)
                self.assertEqual(b'{"value":null}', c.get(url).content)


def load_tests(loader, tests, ignore):
    """ Enable unittest discovery of doctests """
    tests.addTests(doctest.DocTestSuite(views))
    return tests
