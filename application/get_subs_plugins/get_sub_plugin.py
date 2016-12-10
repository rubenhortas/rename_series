#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    get_sub_plugin
"""
import abc
import inspect

from crosscutting.condition_messages import print_exception, print_info
from crosscutting.constants import USER_AGENT
from abc import ABCMeta


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


def execute_plugin(plugin, video_file):
    try:
        plugin = get_plugin_instance(plugin)
        file_found = getattr(plugin, "download")(video_file)

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
