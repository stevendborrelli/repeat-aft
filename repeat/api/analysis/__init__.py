"""
TODO docstring
"""

import logging
import os.path
import pluginbase

logger = logging.getLogger(__name__)

# Plugins that are included in the source when this module is packaged
BASE_PLUGIN_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "plugins")

logger.debug("BASE_PLUGIN_DIR: {}".format(BASE_PLUGIN_DIR))

lmap = lambda *args, **kwargs: list(map(*args, **kwargs))


def get_plugin(variable_name, plugin_paths=[]):
    """ Fetch a plugin named after a variable. Returns a module object. """
    plugin_paths = lmap(os.path.abspath, plugin_paths + [BASE_PLUGIN_DIR])
    logger.debug("Fetching plugin {} from paths {}".format(variable_name,
                                                           plugin_paths))
    # See the README: https://github.com/mitsuhiko/pluginbase
    pbase = pluginbase.PluginBase(package=__name__ + ".plugins")
    psrc = pbase.make_plugin_source(searchpath=plugin_paths)

    return psrc.load_plugin(variable_name)


def extract(text, variable_name, plugin_paths=[]):
    """
    Extract a single variable from a paper. Returns None if no plugin could be
    found to extract that variable.
    """
    return get_plugin(variable_name, plugin_paths).extract(text)
