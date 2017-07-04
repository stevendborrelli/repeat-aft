import django.core.files
import django.core.files.uploadedfile
import django.test
import factory
import faker
import json
import os
import random
import requests
import string

from api import models


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
        self.fake = faker.Faker()

    def test_domain_str(self):
        """ Test that domain's __str__ represents it as JSON """
        name, text = self.fake.name(), self.fake.text()
        dom0 = models.Domain.objects.create(name=name, description=text)
        self.assertEqual(
            str(dom0),
            '{{"name": "{}", "description": "{}"}}'.format(name, text))


class PaperTests(django.test.TestCase):
    class PaperFactory(factory.Factory):
        class Meta:
            model = models.Paper

        title = "🐋"
        authors = json.dumps([faker.Faker().name() for _ in range(5)])
        # Fetch the PDF if we don't already have it
        document = django.core.files.uploadedfile.SimpleUploadedFile(
            "file.pdf", get_pdf("https://arxiv.org/pdf/1706.08508.pdf"))

    def test_paper(self):
        self.assertEqual(
            set(['unique_id', 'title', 'authors', 'domains']),
            set(json.loads(str(self.PaperFactory.create())).keys()))
