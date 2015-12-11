#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    SubtitleFile.py
"""

from crosscutting import constants

from .file import File

LANG_ES = "Español"
COUNTRY_ES = "España"
COUNTRY_ES_STR = "(Español (España))"
CONTRY_LAT = "Latinoamérica"
COUNTRY_LAT_STR = "(Español (Latinoamérica))"
VOS_ES = "VOSE"


class Subtitle(File):

    def __init__(self):
        pass

    def __init__(self, path, file_name, testing):
        super(Subtitle, self).__init__(path, file_name, testing)
        self.ext = constants.DEFAULT_SUBTITLE_EXTENSION
        self.__set_new_name()
        if self.new_file_name:
            self._translate()
            self._rename()

    def __set_new_name(self):
        """
        __set_new_name(self)
            Sets the new file name.
        """

        if LANG_ES in self.file_name:

            self.new_file_name = self.file_name

            if COUNTRY_ES in self.file_name:
                self.new_file_name = self.new_file_name.replace(
                    COUNTRY_ES_STR, VOS_ES)

            elif COUNTRY_LAT_STR in self.new_file_name:
                self.new_file_name = self.new_file_name.replace(COUNTRY_LAT_STR,
                                                                VOS_ES)
