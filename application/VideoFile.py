#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    VideoFile.py
"""

import os
import re

from presentation import Messages

from .Episode import Episode
from .File import File

EXPANDED_NAMES = {
    # American Horror Story
    "AmericanHStory": "American Horror Story",
    "AHS":            "American Horror Story",
    "AmericanStory":  "American Horror Story",

    # Arrow
    "Arr": "Arrow",

    # Bates Motel
    "BMotel":        "Bates Motel",
    "BaMotel":       "Bates Motel",
    "BatesMotel":    "Bates Motel",

    # Boardwalk Empire
    "BoardEmpire":       "Boardwalk Empire",
    "BoardwalkEmpire":   "Boardwalk Empire",
    "BoarEmpire":        "Boardwalk Empire",

    # Bob"s Burgers
    "Bobs Burgers":  "Bob\"s Burgers",

    # Castle
    "Cas": "Castle",

    # Doctor Who
    "DoctorWho":     "Doctor Who",

    # Érase una vez
    "EraseVez":      "Érase una vez (Once upon a time)",
    "Erase Una Vez": "Érase una vez (Once upon a time)",

    # El mentalista
    "EMentalista":   "El mentalista",
    "Mentalista":    "El mentalista",

    # Elementary
    "Ele":      "Elementary",
    "Elem":     "Elementary",
    "Eleme":    "Elementary",
    "Elmntry":  "Elementary",

    # Marvel"s Agents of SHIELD
    "Marvel\"s Agents of S H I E L D":   "Marvel\"s Agents of S.H.I.E.L.D.",
    "Marvels Agents":                    "Marvel\"s Agents of S.H.I.E.L.D.",


    # Ray Donovan
    "RDonovan": "Ray Donovan",

    # South Park
    "SP":        "South Park",
    "SPark":     "South Park",
    "SouthPark": "South Park",

    # The Big Bang Theory
    "TBBTheory":     "The Big Bang Theory",
    "TBiBaTheory":   "The Big Bang Theory",

    # The Walking Dead
    "TWalkDead":     "The Walking Dead",
    "TWalkingDead":  "The Walking Dead",

    # True Detective
    "TDetective":    "True detective",
    "TrDetective":   "True detective",
}

EPISODE_TITLE_PATTERN = re.compile("[\w ]*", re.UNICODE)
YEAR_PATTERN = re.compile(" \d{4}")


class VideoFile(File):
    """
    Class VideoFile
        Stores the data and operations relatives to the video files.
        Child class of cFile.
    """

    episode_in_name = None
    episode_title = None
    ov = False

    def __init__(self, files_path, file_name, testing, debugging):
        super(VideoFile, self).__init__(files_path, file_name, testing,
                                        debugging)

        if self.debugging:
            print()
            Messages.debug_msg("VideoFile __init___")
            Messages.debug_msg("\tself.f_absolute_original_path: {0}".format(self.f_abs_original_path))
            Messages.debug_msg("\tself.file_name: {0}".format(self.file_name))
            Messages.debug_msg("\tis well formated: {0}".format(self.__is_well_formated()))

        if not self.is_well_formated():
            self.__remove_quality()
            self.__get_episode()
            if self.__is_serie():
                self.__set_ov()
                self.__get_show_name()
                self.__wrap_year()
                self.__expand_show_name()
                self.__get_episode_title()
                self.__set_show_name()
                self._File__translate()
                self.f_abs_new_path = os.path.join(self.files_path,
                                                   self.file_name_new)
                self._File__rename()

    def __get_episode(self):
        """
        __get_episode(self)
            Retrieves and stores the data relative to the season and
            episode.
        """
        this_episode = Episode(self.file_name)

        # If is a serie (movies doesn"t have episodes)
        if this_episode.episode_in_name:
            self.episode_in_name = this_episode.episode_in_name
            self.episode = this_episode.episode
            self.new_file_name = self.file_name.replace(self.episode_in_name,
                                                        self.episode)

            if self.debugging:
                Messages.debug_msg("__get_episode")
                Messages.debug_msg("\tself.episode_in_name: {0}".format(self.episode_in_name))
                Messages.debug_msg("\tself.episode: {0}".format(self.episode))
                Messages.debug_msg("\tself.new_file_name: {0}".format(self.new_file_name))

    def __is_serie(self):
        """
        __is_serie(self)
            Returns if the video file is a serie.
        """

        if self.episode_in_name:
            return True
        else:
            return False

    def __get_show_name(self):
            """
            __get_show_name(self)
                Gets the show name and if it's in original version.
            """

            self.extension = os.path.splitext(self.file_name)[1]
            file_name = os.path.splitext(self.file_name)[0]

            list_file_name = file_name.split(self.episode_in_name)

            show_name = list_file_name[0]
            show_name = show_name.replace(".", " ")
            show_name = show_name.strip()

            self.show_name = show_name

            # DEBUG
            if self.debugging:
                Messages.debug_msg("__get_show_name")
                Messages.debug_msg("\tself.show_name: {0}".format(self.show_name))

    def __expand_show_name(self):
        """
        __expand_show_name(self)
            Expands some serie titles.
        """

        if self.show_name in EXPANDED_NAMES:
            self.show_name = EXPANDED_NAMES.get(self.show_name)

            if self.debugging:
                Messages.debug_msg("__expand_show_name")
                Messages.debug_msg("\texpanded_name: {0}".format(self.show_name))
        else:
            if self.debugging:
                Messages.debug_msg("{0} will be not expanded".format(self.show_name))

    def __get_episode_title(self):

            file_name = os.path.splitext(self.file_name)[0]

            list_file_name = file_name.split(self.episode_in_name)

            show_name = list_file_name[1]

            if show_name:
                title_match = EPISODE_TITLE_PATTERN.search(show_name)

                if title_match:
                    episode_title = title_match.group(0).strip()

                    if episode_title != "":
                        self.episode_title = episode_title

                        # DEBUG
                        if self.debugging:
                            Messages.debug_msg("__get_episode_title")
                            Messages.debug_msg("\tself.episode_title: {0}".format(self.episode_title))

    def __set_ov(self):
        """
        __set_ov(self)
            Sets if the file is in Original Version.
        """

        # Get and set if the file is in original version
        if "newpct" not in self.file_name:
            self.ov = True

    def __wrap_year(self):
        """
        __wrap_year(self)
            Wraps the year (if exists) into parentheses.
        """

        year_match = YEAR_PATTERN.search(self.show_name)

        if year_match:
            year_in_show_name = year_match.group(0).lstrip()
            new_year = "(" + year_in_show_name + ")"
            self.show_name = self.show_name.replace(year_in_show_name, new_year)

    def __set_show_name(self):
        """
        __set_show_name(self)
            Sets the output title.
        """

        # Do not change if the year is in the title
        if self.episode_in_name not in self.show_name:

            new_file_name = self.show_name + " " + self.episode

            if self.episode_title:
                new_file_name = new_file_name + " - " + self.episode_title

            if self.ov:
                new_file_name = new_file_name + " (VO)"

            self.file_name_new = new_file_name + self.extension

        else:
            self.file_name_new = self.file_name

    def __remove_quality(self):
        """
        __remove_quality(self)
            Removes video quality from file
        """

        if "720p" in self.file_name:
            self.file_name = self.file_name.replace("720p", "")
        elif "1080p" in self.file_name:
            self.file_name = self.file_name.replace("1080p", "")

        self.file_name = self.file_name.replace("..", ".")
        self.file_name = self.file_name.strip()
