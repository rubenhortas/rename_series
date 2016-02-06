#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      file.py
"""

import os
import re

from crosscutting.condition_messages import print_exception
from crosscutting.constants import EXPANDED_NAMES
from crosscutting.constants import OV_TRACKERS
from crosscutting.constants import QUALITIES
from crosscutting.constants import TRANSLATED_NAMES
from domain.utils.file_handler import mv
from .episode import Episode

EPISODE_TITLE_PATTERN = re.compile("[\w ]*", re.UNICODE)
IS_WELL_FORMATTED_COMPILED_PATTERN = re.compile(
    "^[\w \(\)]*[\d]{1,2}x[\d]{1,2}", re.UNICODE)
YEAR_PATTERN = re.compile(" \(?\d{4}\)?")


class File(object):
    episode = None
    episode_title = None
    episode_in_file_name = None
    extension = None
    file_name = None
    new_file_name = None
    new_path = None
    original_path = None
    original_version = False
    path = None
    season = None
    show_name = None

    def __init__(self, path, file_name, testing):
        self.path = path
        self.file_name = file_name
        self.original_path = os.path.join(path, self.file_name)
        self.testing = testing
        self.extension = os.path.splitext(self.file_name)[1]

    def is_well_formatted(self):
        """
        is_well_formatted(self)
            Returns if the file is well formatted
            Well formatted = show_name 0x00 [episode name].avi
        """

        if IS_WELL_FORMATTED_COMPILED_PATTERN.match(self.file_name):
            return True
        else:
            return False

    def _remove_quality(self):
        """
        _remove_quality(self)
            Removes video quality from file name.
        """

        for quality in QUALITIES:
            if quality in self.file_name:
                self.file_name = self.file_name.replace(quality, "")

        if ".." in self.file_name:
            self.file_name = self.file_name.replace("..", ".")

        self.file_name = self.file_name.strip()

    def _set_episode(self):
        """
        _set_episode(self)
            Retrieves and stores the data relative to the season and
            episode.
        """

        episode = Episode(self.file_name)

        if episode.episode_in_file_name:
            self.episode_in_file_name = episode.episode_in_file_name
            self.episode = episode.episode_formatted
            self.new_file_name = self.file_name.replace(self.episode_in_file_name, self.episode)

    def _is_show(self):
        """
        _is_show(self)
            Returns if the video file is a show.
        """

        if self.episode_in_file_name:
            return True
        else:
            return False

    def _set_ov(self):
        """
        _set_ov(self)
            Sets if the file is in Original Version.
        """

        for tracker_name in OV_TRACKERS:
            if tracker_name in self.file_name:
                self.original_version = True
                break

    def _set_show_name(self):
        """
        _set_show_name(self)
            Gets the show name and if it's in original version.
        """

        file_name = os.path.splitext(self.file_name)[0]

        show_name = file_name.split(self.episode_in_file_name)[0]
        show_name = show_name.replace(".", " ")
        show_name = show_name.strip()

        self.show_name = show_name

    @staticmethod
    def _wrap_year(attribute):
        """
        _wrap_year(self)
            Wraps the year (if exists) into parentheses.
        Arguments:
            - attribute: (string) Attribute where the year will be formatted.
        """

        formatted_attribute = attribute
        year_match = YEAR_PATTERN.search(attribute)

        if year_match:
            year_in_show_name = year_match.group(0).strip()

            if "(" not in year_in_show_name or ")" not in year_in_show_name:
                new_year = "({0})".format(year_in_show_name)
                formatted_attribute = formatted_attribute.replace(year_in_show_name, new_year)

        return formatted_attribute

    def _expand_show_name(self):
        """
        _expand_show_name(self)
            Expands some show titles.
        """

        if self.show_name.lower() in EXPANDED_NAMES:
            self.show_name = EXPANDED_NAMES.get(self.show_name.lower())

    def _set_episode_title(self):

        file_name = os.path.splitext(self.file_name)[0]

        file_name_splitted = file_name.split(self.episode_in_file_name)

        if file_name_splitted[1]:
            match = EPISODE_TITLE_PATTERN.search(file_name_splitted[1])

            if match:
                episode_title = match.group(0).strip()

                if episode_title != "":
                    self.episode_title = episode_title

    def _set_new_file_name(self):
        """
        __set_show_name(self)
            Sets the output title.
        """

        new_file_name = "{0} {1}".format(self.show_name, self.episode)

        if self.episode_title:
            new_file_name = "{0} {1}".format(new_file_name, self.episode_title)

        if self.original_version:
            new_file_name = "{0} {1}".format(new_file_name, self.original_version)

        self.new_file_name = "{0}{1}".format(new_file_name, self.extension)

    def _translate(self):
        """
         _translate(self)
            Translates some series names.
        """

        if self.show_name in TRANSLATED_NAMES:
            translated_show_name = TRANSLATED_NAMES.get(self.show_name)
            self.new_file_name = self.new_file_name.replace(self.show_name, translated_show_name)

    def _rename_file(self):
        """
        _rename_file(self)
            Renames a file with a new name.
        """

        try:
            if self.new_file_name and self.new_file_name != self.file_name:
                self.new_path = os.path.join(self.path, self.new_file_name)

                mv(self.original_path, self.new_path, self.testing)

        except Exception as ex:
            print_exception(ex)
