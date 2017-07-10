"""\
Testing views is really more like integration testing than unit testing, but it
shouldn't matter too much.\
"""

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
            paper = factories.Paper.create(document=factory.django.FileField(data=document))
            c = django.test.Client()
            url = "{}/extract/{}/{}".format(BASE_URL, paper.unique_id, "funding")
            self.assertEqual(b'{"value":null}', c.get(url).content)
