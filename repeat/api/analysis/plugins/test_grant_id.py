import faker
import functools
import logging
import unittest

from . import grant_id

fake = faker.Faker()

TESTS = [
    ("This research was funded by the NIH (grant id: #102).", "102"),
    ("We received funding from Reed College (grant 8CGZ).", "8CGZ")
]


class Test(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.WARNING)
        self.extract = functools.partial(grant_id.extract, logger=logger)

    def test_grant_id(self):

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
