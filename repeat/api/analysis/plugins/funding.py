import functools
import logging
import nltk

from . import re_util

logger = logging.getLogger(__name__)


def extract(text, logger=logger):
    """ See Variables.objects.get(pk="funding") and the file test_funding.py """

    search_any = functools.partial(re_util.search_any, logger=logger)

    for sentence in nltk.sent_tokenize(text):
        if search_any([r'funded.*?by', r'funding.*?from'], sentence):
            # yapf: disable
            match = search_any([
                # e.g. "This research was funded by a grant from <name>"
                r'grant.*?from (.*?)[^\w\s-]',
                # e.g. "This research was funded by <name>"
                r'funded.*?by (.*?)[^\w\s-]',
                # e.g. "We received funding from <name>"
                r'funding.*from (.*?)[^\w\s-]'
            ], sentence)
            # yapf: enable
            try:
                return (match.group(1).strip(), sentence)
            except AttributeError:  # no match was found
                return None
    return None
