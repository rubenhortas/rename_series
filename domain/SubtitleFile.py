#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    SubtitleFile.py
"""

from .File import File


class SubtitleFile(File):

    def __init__(self, files_path, file_name, testing, debugging):
        super(SubtitleFile, self).__init__(files_path, file_name, testing,
                                           debugging)
        self.ext = '.srt'
        self.__set_new_name()
        if self.file_name != self.file_name_new:
            self._File__translate()
            self._File__rename()

    def __set_new_name(self):
        """
        __set_new_name(self)
            Sets the new file name.
        """

        self.file_name_new = self.file_name

        if 'Español' in self.file_name_new:
            if 'España' in self.file_name:
                self.file_name_new = self.file_name_new.replace('(Español (España))', 'VOSE')
            elif 'Latinoamérica' in self.file_name_new:
                self.file_name_new = self.file_name_new.replace('(Español (Latinoamérica))',
                                                                'VOSE')
