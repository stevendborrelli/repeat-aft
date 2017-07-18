import doctest
import os
import unittest

from pdfutil import pdfutil


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


HERE = os.path.abspath(os.path.dirname(__file__))
BLANK_PATH = os.path.join(HERE, "blank.pdf")
BLANK = read_bytes(BLANK_PATH)
LOREM_PATH = os.path.join(HERE, "lorem.pdf")
LOREM = read_bytes(LOREM_PATH)

BLANK_RESULT = "\x0c"
LOREM_RESULT = ("Lorem Ipsum is the dummy text of the typesetting industry."
                "\n\n\x0c")


class PDFUtilTests(unittest.TestCase):
    def test_pdf_file_to_text(self):
        self.assertEqual(BLANK_RESULT, pdfutil.pdf_file_to_text(BLANK_PATH))
        self.assertEqual(LOREM_RESULT, pdfutil.pdf_file_to_text(LOREM_PATH))

    def test_pdf_to_text(self):
        self.assertEqual(BLANK_RESULT, pdfutil.pdf_to_text(BLANK))
        self.assertEqual(LOREM_RESULT, pdfutil.pdf_to_text(LOREM))


def load_tests(loader, tests, ignore):
    """ Enable unittest discovery of doctests """
    tests.addTests(doctest.DocTestSuite(pdfutil))
    return tests
