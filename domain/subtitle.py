#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    subtitle.py
"""

import os
from crosscutting.constants import OV_SUBTITLES
from .file import File


class Subtitle(object, File):

    def __init__(self, path, file_name, testing):
        super(Subtitle, self).__init__(path, file_name, testing)

        if not self.is_well_formatted():
            self._remove_quality()
            self._set_episode()
            if self._is_show():
                self._set_ov()
                self._set_show_name()
                self.show_name = self._wrap_year(self.show_name)
                self._expand_show_name()
                self._set_episode_title()
                self._set_new_file_name()
                self._translate()
                self.new_path = os.path.join(self.path, self.new_file_name)
        else:
            self.__set_new_name()
            if self.new_file_name:
                self._translate()

        self._rename_file(testing)

    def __set_new_name(self):
        """
        __set_new_name(self)
            Sets new file name.
        """

        for language in OV_SUBTITLES:
            if language in self.file_name:
                file_name = self.file_name
                self.new_file_name = file_name.replace(
                    language, OV_SUBTITLES.get(language))
