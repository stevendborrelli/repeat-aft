#!/usr/bin/env python
from setuptools import setup

setup(
    name="repeat-aft",
    version="0.1.0",
    description="",
    package_dir={"": "repeat"},
    include_package_data=True,
    packages=["pdfutil", "repeat", "api"],
    scripts=["repeat/manage.py", "repeat/tests.py"],
    zip_safe=False,
    test_suite="tests.runtests")
