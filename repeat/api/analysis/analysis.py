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
lfilter = lambda *args, **kwargs: list(filter(*args, **kwargs))


def extract(text, variable_name, plugin_paths=[], logger=logger):
    """
    Extract a single variable from a paper. Returns None if no plugin could be
    found to extract that variable.
    """
    plugin_paths = lmap(os.path.abspath, plugin_paths + [BASE_PLUGIN_DIR])
    logger.debug("Fetching plugin {} from paths {}".format(variable_name,
                                                           plugin_paths))

    # See the README: https://github.com/mitsuhiko/pluginbase
    plugin_base = pluginbase.PluginBase(package=__name__ + ".internal")
    plugin_source = plugin_base.make_plugin_source(searchpath=plugin_paths)

    plugin_list = lfilter(lambda n: not n.startswith("test_"),
                          plugin_source.list_plugins())
    logger.debug("Plugin list: {}".format(plugin_list))

    plugin = plugin_source.load_plugin(variable_name)

    # NB: we _must_ call plugin.extract in the same function as the plugin is
    # imported/loaded, otherwise some weird black magic happens.
    return plugin.extract(text, logger=logger)
