import functools
import logging
import re

logger = logging.getLogger(__name__)

search = functools.partial(re.search, flags=re.IGNORECASE | re.DOTALL)


def search_any(patterns, text, logger=logger):
    """ Given a list of regexes, return either the first match or None """
    for pattern in patterns:
        logger.debug("Searching text {} for {}".format(text, pattern))
        result = search(pattern, text)
        if result is not None:
            return result
    logger.debug("Returning None")
    return None
