#!/usr/bin/env python3

# Run with `python3 setup.py test`
# Code taken from
# https://docs.djangoproject.com/en/1.11/topics/testing/advanced/

import doctest
import os
import os.path
import sys
import unittest

import django
from django.conf import settings
from django.test.utils import get_runner

HERE = os.path.dirname(os.path.abspath(__file__))

def runtests():
    os.environ["DJANGO_SETTINGS_MODULE"] = "repeat.settings"
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests([HERE])
    sys.exit(bool(failures))

if __name__ == "__main__":
    runtests()
