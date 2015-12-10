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

# from crosscutting import condition_messages
# from crosscutting import messages_move_series
import domain.utils.file_handler


IS_WELL_FORMATED_COMPILED_PATTERN = re.compile(
    "^[\w \(\)]*[\d]{1,2}x[\d]{1,2}", re.UNICODE)


class File:
    """
    Class File
            Superclass that stores data and operations common
            to child classes videofile and subtitlefile.
    """

    episode = None
    extension = None
    file_name = None
    file_new_name = None
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
        __is_well_formated(self)
            Returns if the file is well formated
            Well formated = show_name SExEP [ ...].extension =
            = show_name 0x00 [episode name].avi
        """

        if IS_WELL_FORMATED_COMPILED_PATTERN.match(self.file_name):
            return True
        else:
            return False

    def _rename(self):
        """
        _rename(self)
            Renames a file with a new name.
        """

        self.new_path = os.path.join(self.path, self.file_name_new)

        if self.testing:
            self.__print_move()

        file_handler.mv(self.original_path, self.new_path,
                        self.debugging, self.testing)

#     def _print_move(self):
#         """
#         __print_move(self)
#         Displays the original file name and the new file name.
#         """
#
#         if self.file_name != self.file_name_new:
#             messages_move_series.mv_msg(self.file_name, self.file_name_new)
#
#     def _translate(self):
#         """
#          __translate(self)
#             Translates some series names.
#         """
#
#         name = self.show_name
#
#         if name in TRANSLATED_NAMES:
#             translated_name = TRANSLATED_NAMES.get(name)
#             self.file_name_new = self.file_name_new.replace(name,
#                                                             translated_name)
