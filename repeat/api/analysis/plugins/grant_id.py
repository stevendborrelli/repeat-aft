import functools
import logging
import nltk

from . import re_util

logger = logging.getLogger(__name__)


def extract(text, logger=logger):
    """ See Variables.objects.get(pk="extract") and the file test_grant_id.py """

    search_any = functools.partial(re_util.search_any, logger=logger)

    for sentence in nltk.sent_tokenize(text):
        if search_any([r'funded.*?by', r'funding.*?from'], sentence):
            # yapf: disable
            match = search_any([
                # e.g. "This research was funded by Reed College (grant id: #102)"
                "grant.*?(\w*\d[\w\d/-]*)"
            ], sentence)
            # yapf: enable
            try:
                return (match.group(1).strip(), sentence)
            except AttributeError:  # no match was found
                return None
    return None
