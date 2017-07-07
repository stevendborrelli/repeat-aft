import faker
import functools
import logging
import unittest

from . import funding

fake = faker.Faker()

TESTS = [
    ("This research was funded by the NIH.", "the NIH"),
    ("This program was funded in part by our member stations.",
        "our member stations"),
    ("We received funding from Reed College.", "Reed College"),
    ("We received funding and technical support from Reed College.",
    "Reed College")
]

class TestFunding(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.WARNING)
        self.extract = functools.partial(funding.extract, logger=logger)

    def test_funding(self):

        # Surround a sentence with a bunch of randomly generated text
        pad = lambda sentence: " ".join([fake.text(), sentence, fake.text()])

        # Does ``extract`` 1. Find the relevant sentence and 2. extract the
        # relevant portion?
        for sentence, result in TESTS:
            self.assertEqual((result, sentence), self.extract(pad(sentence)))

        # Negatives
        self.assertIsNone(self.extract("funded by"))
        for _ in range(10):
            self.assertIsNone(self.extract(fake.text()))
