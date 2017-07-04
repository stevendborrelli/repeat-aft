import functools
import logging
import nltk
import re

logger = logging.getLogger(__name__)


def extract(text, logger=logger):
    """ TODO: docstring """

    search = functools.partial(re.search, flags=re.IGNORECASE | re.DOTALL)

    def search_any(patterns, text):
        """ Given a list of regexes, return either the first match or None """
        for pattern in patterns:
            logger.debug("Searching text {} for {}".format(text, pattern))
            result = search(pattern, text)
            if result is not None:
                return result
        logger.debug("Returning None")
        return None

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
