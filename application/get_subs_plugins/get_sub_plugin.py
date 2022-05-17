import abc
import inspect
import os
from abc import ABCMeta

from crosscutting.condition_messages import print_exception, print_info
from crosscutting.constants import USER_AGENT
from domain.video import Video


class GetSubsPlugin(object, metaclass=ABCMeta):
    """
    Base class for plugins.
    """

    name = None
    url = None
    user_agent = None

    def __init__(self, name, url):
        self.user_agent = USER_AGENT
        self.name = name
        self.url = url

    @abc.abstractmethod
    def download(self, file_name):
        # Should return the result of find and download a file (true/false)
        print_info("\tSearching for {0} in {1}...".format(file_name, self.name, self.url))


def execute_plugin(plugin, f):
    try:
        video = _get_file_info(f)

        plugin = get_plugin_instance(plugin)
        file_found = getattr(plugin, "download")(f)

        return file_found
    except Exception as e:
        print_exception(e)


def get_plugin_instance(plugin_name):
    try:
        class_name = inspect.getmembers(plugin_name, inspect.isclass)[1][0]
        plugin_class = getattr(plugin_name, class_name)
        plugin_instance = plugin_class()

        return plugin_instance
    except Exception as e:
        print_exception(e)


def _get_file_info(f):
    f_path = os.path.dirname(f)
    f_name = os.path.basename(f)
    video = Video(f_path, f_name, False)
    return video
