from django.test import TestCase

from . import models

# Create your tests here.


class DomainTests(TestCase):
    def setUp(self):
        models.Domain.objects.create(name="dom0", description="test description")

    def test_domain_repr(self):
        """ Test that domain's __repr__ represents it as JSON """
        dom0 = models.Domain.objects.get(name="dom0")
        self.assertEqual(
            str(dom0), '{"name": "dom0", "description": "test description"}')
