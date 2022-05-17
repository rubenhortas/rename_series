import importlib
import os

from crosscutting.condition_messages import print_info, print_error, print_exception
from domain.utils.file_handler import is_python


def load_plugins():
    loaded_modules = []

    base_path = os.getcwd()
    plugins_path = os.path.join(base_path, "application", "get_subs_plugins")

    print_info("Loading plugins...")

    if os.path.exists(plugins_path):
        plugins = _get_plugins(plugins_path)

        if plugins and len(plugins) > 0:
            loaded_modules = _load_modules(plugins)
            print_info("Plugins loaded")
        else:
            print_info("No plugins found to download subtitles")
    else:
        print_error("Plugins not found")

    return loaded_modules


def _get_plugins(path):

    plugins = []

    try:
        plugins_path_files = os.listdir(path)

        for f in plugins_path_files:
            f_abs_path = os.path.join(path, f)
            if os.path.isfile(f_abs_path):
                if is_python(f_abs_path):
                    plugins.append(f)

        plugins.remove("__init__.py")
        plugins.remove("get_sub_plugin.py")

        return plugins
    except ValueError:
        pass
    except Exception as e:
        print_exception(e)


def _load_modules(plugins):
    try:
        loaded_modules = []

        for plugin in plugins:
            plugin_name = os.path.splitext(plugin)[0]
            plugins_module = ".get_subs_plugins"
            plugin_relative_path = "{0}.{1}".format(plugins_module, plugin_name)
            plugin_loaded = importlib.import_module(plugin_relative_path, __package__)
            loaded_modules.append(plugin_loaded)
            print_info("\t+ {0} loaded".format(plugin_name))

        return loaded_modules
    except Exception as e:
        print_exception(e)
