#!/usr/bin/env python3

# Run with `python3 setup.py test`
# Code taken from
# https://docs.djangoproject.com/en/1.11/topics/testing/advanced/

import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

def runtests():
    os.environ["DJANGO_SETTINGS_MODULE"] = "repeat.settings"
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests([
        "api.tests",
        "api.analysis.tests",
        "api.analysis.plugins",
        "pdfutil"
    ])
    sys.exit(bool(failures))

if __name__ == "__main__":
    runtests()
