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

BASE_URL = "/api/v0"
EXTRACT_URL = BASE_URL + "/extract"


class ViewTests(django.test.TestCase):
    fixtures = ["fixture.json"]

    def test_extract(self):
        """ Test that variables are extracted properly """
        for document in [test_pdfutil.BLANK, test_pdfutil.LOREM]:
            paper = factories.Paper.create(document=factory.django.FileField(
                data=document))
            paper_url = "{}/{}".format(EXTRACT_URL, paper.unique_id)

            c = django.test.Client()
            variables = ["funding", "grant_id"]
            for var in variables:
                var_url = "{}/{}".format(paper_url, var)
                self.assertEqual(b'{"value":null}', c.get(var_url).content)

            # Extract all at once
            self.assertEqual(b'{"funding":null,"grant_id":null}',
                             c.get(paper_url).content)

    def test_malformed_pdf(self):
        """ Uploading a malformed PDF leads to an error, not a crash """
        paper = factories.Paper.create(document=factory.django.FileField(
            data=b""))
        paper_url = "{}/{}".format(EXTRACT_URL, paper.unique_id)
        c = django.test.Client()
        # Extract all at once
        d = json.loads(c.get(paper_url).content)
        self.assertEqual({"error"}, set(d.keys()))


def load_tests(loader, tests, ignore):
    """ Enable unittest discovery of doctests """
    tests.addTests(doctest.DocTestSuite(views))
    return tests
