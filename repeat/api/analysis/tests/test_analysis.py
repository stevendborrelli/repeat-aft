import django.test
import functools
import logging
import os.path
import sys

from .. import analysis

from ..plugins import test_funding


class PluginTests(django.test.TestCase):
    def setUp(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.WARNING)
        logger.addHandler(logging.StreamHandler(sys.stdout))
        self.extract = functools.partial(analysis.extract, logger=logger)

    def test_modulenotfound(self):
        """ When a module isn't found, an exception should be raised """
        self.assertRaises(ImportError, self.extract, "", "fake_name")

    def test_dummy_plugin(self):
        """ Call a dummy plugin """
        path = os.path.dirname(os.path.abspath(__file__))
        result = self.extract("", "test_plugin", plugin_paths=[path])
        self.assertEqual(True, result)

    def test_actual_plugin(self):
        """ Call the "funding" plugin """
        for sentence, result in test_funding.TESTS:
            self.assertEqual(
                (result, sentence), self.extract(sentence, "funding"))
