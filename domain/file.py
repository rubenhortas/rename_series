#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      File.py
"""

import os
import re

from crosscutting import condition_messages
from crosscutting import constants
from crosscutting import messages_move_series
from domain.utils import file_handler


IS_WELL_FORMATED_COMPILED_PATTERN = re.compile(
    "^[\w \(\)]*[\d]{1,2}x[\d]{1,2}", re.UNICODE)
YEAR_PATTERN = re.compile(" \(?\d{4}\)?")


class File:

    episode = None
    extension = None
    file_name = None
    new_file_name = None
    new_path = None
    original_path = None
    path = None
    season = None
    show_name = None
    testing = False

    def __init__(self, path, file_name, testing):
        self.path = path
        self.file_name = file_name
        self.original_path = os.path.join(path, self.file_name)
        self.testing = testing

    def is_well_formatted(self):
        """
        is_well_formatted(self)
            Returns if the file is well formated
            Well formatted = show_name 0x00 [episode name].avi
        """

        if IS_WELL_FORMATED_COMPILED_PATTERN.match(self.file_name):
            return True
        else:
            return False

#     def _print_move(self):
#         """
#         _print_move(self)
#         Displays the original file name and the new file name.
#         """
#
#         if self.file_name != self.new_file_name:
#             messages_move_series.mv_msg(self.file_name, self.new_file_name)

    def _translate(self):
        """
         _translate(self)
            Translates some series names.
        """

        if self.show_name in constants.TRANSLATED_NAMES:
            translated_show_name = constants.TRANSLATED_NAMES.get(
                self.show_name)
            self.new_file_name = self.new_file_name.replace(
                self.show_name, translated_show_name)

    def _rename(self):
        """
        _rename(self)
            Renames a file with a new name.
        """

        try:
            self.new_path = os.path.join(self.path, self.new_file_name)

            file_handler.mv(self.original_path, self.new_path, self.testing)
        except Exception as ex:
            condition_messages.print_exception(ex)

    def _wrap_year(self, attribute):
        """
        _wrap_year(self)
            Wraps the year (if exists) into parentheses.
        Arguments:
            - attribute: (string) Attribute where the year will be formatted.
        """

        year_match = YEAR_PATTERN.search(attribute)

        if year_match:
            year_in_show_name = year_match.group(0).strip()

            if "(" not in year_in_show_name or ")" not in year_in_show_name:
                new_year = "({0})".format(year_in_show_name)
                attribute = attribute.replace(year_in_show_name, new_year)
