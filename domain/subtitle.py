#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    SubtitleFile.py
"""

from pathlib import Path

from crosscutting.constants import DEFAULT_SUBTITLE_EXTENSION
from file import File


class SubtitleFile(File):

    def __init__(self, path, file_name, testing):
        self.path = path
        self.file_name = file_name
        self.testing = testing
        self.ext = DEFAULT_SUBTITLE_EXTENSION
        self.__set_new_name()
        if self.file_name != self.new_file_name:  # Es none?
            self._translate()
            self._rename()

    def __set_new_name(self):
        """
        __set_new_name(self)
            Sets the new file name.
        """

        self.new_file_name = self.file_name

        if 'Español' in self.new_file_name:
            if 'España' in self.file_name:
                self.new_file_name = self.new_file_name.replace(
                    '(Español (España))', 'VOSE')
            elif 'Latinoamérica' in self.new_file_name:
                self.new_file_name = self.new_file_name.replace('(Español (Latinoamérica))',
                                                                'VOSE')
