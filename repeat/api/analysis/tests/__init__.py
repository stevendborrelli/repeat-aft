import django.test
import logging
import os.path
import sys

from api.analysis import extract


class PluginTests(django.test.TestCase):
    def setUp(self):
        logger = logging.getLogger("api.analysis")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler(sys.stdout))

    def test_modulenotfound(self):
        """ When a module isn't found, an exception should be raised """
        self.assertRaises(ModuleNotFoundError, extract, "", "fake_name")

    # def test_plugin(self):
    #     """ Call a dummy plugin """
    #     path = os.path.dirname(os.path.abspath(__file__))
    #     self.assertEqual(True, extract("", "test_plugin", plugin_paths=[path]))
