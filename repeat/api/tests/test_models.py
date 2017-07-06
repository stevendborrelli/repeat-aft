import django.core.files
import django.core.files.uploadedfile
import django.test
import json

from . import factories
from pdfutil import test_pdfutil

from .. import models


class DomainTests(django.test.TestCase):
    def test_domain_str(self):
        """ Test that domain's __str__ represents it as JSON """
        dom0 = factories.Domain.create()
        json_str = '{{"name": "{}", "description": "{}"}}'.format(
            dom0.name, dom0.description)
        self.assertEqual(str(dom0), json_str)


class PaperTests(django.test.TestCase):
    def test_paper(self):
        paper = factories.Paper.create()
        self.assertEqual(
            set(['unique_id', 'title', 'authors', 'domains']),
            set(json.loads(str(paper)).keys()))
