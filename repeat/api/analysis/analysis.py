""" TODO: documentation for the plugin architecture """

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
    """ Attempt to extract a single variable from a paper.

    Args:
        text: The full text of the paper
        variable_name: See models.Variable.name
        plugin_paths: Directory in which to search for plugins
        logger: An instance of Python's standard logging class

    Returns:
        The result of calling the plugin's ``extract`` function.

    Raises:
        ModuleNotFoundError: When there is no such plugin
        ImportError: Python 3.5 has no ModuleNotFoundError

    Examples:

        >>> try:
        ...    extract("", "phony_name")
        ... except ImportError: # Python 3.5 compat
        ...    pass
        ...

        >>> # There is a plugin for the "funding" variable
        >>> extract("This research was funded by Wayne Enterprises.", "funding")
        ('Wayne Enterprises', 'This research was funded by Wayne Enterprises.')

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
