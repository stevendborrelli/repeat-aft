from django.core.files import uploadedfile
import django.core.files
import django.core.files.uploadedfile
import django.test
import factory
import faker
import io
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

    def test_update_file(self):
        paper = factories.Paper.create()
        content = faker.Faker().text().encode()

        # The paper initially has no document_text
        with self.assertRaises(ValueError):
            paper.document_text.file

        paper.document_text = uploadedfile.SimpleUploadedFile("test.dat",
                                                              content)
        paper.save()

        self.assertEqual(content, paper.document_text.read())

    def test_get_text(self):
        # Initially has no document_text attribute
        blank_paper = factories.Paper.create()
        self.assertEqual(
            (test_pdfutil.BLANK_RESULT, False), blank_paper.get_text())
        self.assertEqual(
            (test_pdfutil.BLANK_RESULT, True), blank_paper.get_text())

        lorem_paper = factories.Paper.create(document=factory.django.FileField(
            data=test_pdfutil.LOREM))

        self.assertEqual(
            (test_pdfutil.LOREM_RESULT, False), lorem_paper.get_text())
        self.assertEqual(
            (test_pdfutil.LOREM_RESULT, True), lorem_paper.get_text())
