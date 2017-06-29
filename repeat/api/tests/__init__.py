import django.core.files
import django.core.files.uploadedfile
import django.test
import os
import json
import random
import requests
import string

from .. import models

# Create your tests here.

# TODO: random creation of Model instances?


def random_string(length):
    return "".join(
        random.choice(string.ascii_lowercase) for i in range(length))


def get_pdf(remote_url, local_name="test.pdf"):
    """ Cache a remote PDF """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), local_name)
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        content = requests.get(remote_url).content
        with open(path, "wb") as f:
            f.write(content)

    return content


class DomainTests(django.test.TestCase):
    def setUp(self):
        models.Domain.objects.create(
            name="dom0", description="test description")

    def test_domain_str(self):
        """ Test that domain's __str__ represents it as JSON """
        dom0 = models.Domain.objects.get(name="dom0")
        self.assertEqual(
            str(dom0), '{"name": "dom0", "description": "test description"}')


class PaperTests(django.test.TestCase):
    def setUp(self):
        # Fetch the PDF if we don't already have it
        content = get_pdf("https://arxiv.org/pdf/1706.08508.pdf")

        self.assertNotEqual(b"", content)

        paper0 = models.Paper.objects.create(**{
            "unique_id": "doi:000",
            "title": "🐋",
            "authors": "Langston Barrett",
            "document":
            django.core.files.uploadedfile.SimpleUploadedFile("file.pdf",
                                                              content)
        })

    def test_paper(self):
        paper0 = models.Paper.objects.get(title="🐋")
        self.assertEqual(set(['unique_id', 'title', 'authors', 'domains']),
                         set(json.loads(str(paper0)).keys()))

    # class VariableTests(django.test.TestCase):

    #     def setUp(self):
    #         dom1 = models.Domain.objects.create(name="dom1", description="dom1 description")
    #         cat0 = models.Category.objects.create(name="cat0", description="cat0 description", order=0)
    #         models.Binary.objects.create(name="bin0", domains=[dom1], category=cat0, label="bin0 description")
    #         models.Binary.objects.create(name="bin1", domains=[dom1], category=cat0, label="bin1 description")
    #         models.OneFromMany.objects.create(name="ofm0", domains=[dom1], category=cat0, label="bin1 description")

    #     def test_variables(self):
    #         """ Test getting variables from a domain """
    #         self.assertEqual(models.Variable.objects.filter(domains__name__exact="dom1"), [])
