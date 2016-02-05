#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    show_path.py
"""

import os
import re

FILE_WELL_FORMATED_PATTERN = re.compile(
    "(?P<season>[\d]{1,2})x(?P<episode>[\d]{1,2})(?P<episode_title>[\w \-\(\)])?\.(?P<extension>[\w]{3})", re.UNICODE)


class Path():
    """
    Path
        Stores the information relative to a file and its destiny path.
    """

    show_name = None
    season = None
    season_path = None
    episode = None
    episode_title = None
    extension = None
    final_dest = None

    def __init__(self, file_name, dest, testing):

        match = FILE_WELL_FORMATED_PATTERN.search(file_name)

        if match:
            self.season = match.group("season")
            self.episode = match.group("episode")
            self.episode_title = match.group("episode_title")
            self.extension = match.group("extension")
            self.show_name = file_name.split(self.season)[0].strip()

            name_tmp = "{0}x{1}".format(self.season, self.episode)

            if self.episode_title is not None:
                name_tmp = "{0} - {1}".format(name_tmp,
                                                    self.episode_title)

            file_final_name = "{0}.{1}".format(name_tmp, self.extension)

            if self.__path_exists(dest):
                self.season_path = "{0} {1}".format(SEASON_PATH_NAME,
                                                    self.season)
                if not self.__season_exists(dest):
                    self.__create_season_dir(dest, testing)

                self.final_dest = os.path.join(dest, self.show_name,
                                               self.season_path, file_final_name)

    def __path_exists(self, path):
        """
        __path_exists(self, path)
            Checks if already exists the path for the show in the destiny
            directory.
        Arguments:
            - path: (string) Current destiny path for the files.
        """

        dest = os.path.join(path, self.show_name)
        return os.path.isdir(dest)

    def __season_exists(self, path):
        """
        __season_exists(self, path)
            Checks if already exists the path for the season in the
            destiny directory.
        Arguments:
            - path: (string) Current destiny path for the files.
        """

        season_path = os.path.join(path, self.show_name, self.season_path)
        return os.path.isdir(season_path)

    def __create_season_dir(self, path, debugging, testing):
        """
        __create_season_dir(self, path)
            Creates the season path for the file in the destiny path.
        Arguments:
            - path: (string) Current destiny path for the files.
        """

        season_path = os.path.join(path, self.show_name, self.season_path)

        if not testing:
            os.mkdir(season_path)
