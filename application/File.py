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

from presentation import Messages
import utils.FileHandler as FilesHandler


IS_WELL_FORMATED_COMPILED_PATTERN = re.compile("^[\w \(\)]*[\d]{1,2}x[\d]{1,2}", re.UNICODE)

TRANSLATED_NAMES = {
    "Family Guy":   "Padre de familia",
    "Marvels Agents of S H I E L D": "Marvel\"s Agents Of S.H.I.E.L.D.",
    "Supernatural": "Sobrenatural",
    "The Simpsons": "Los Simpson",
    "Warehouse 13": "Almacén 13",
    "Warehouse13": "Almacén 13"
}


class File:
    """
    Class File
            Superclass that stores data and operations common
            to child classes videofile and subtitlefile.
    """

    files_path = ""
    f_abs_original_path = ""  # Absolute orignal file path
    f_abs_new_path = ""
    file_name = ""
    file_name_new = ""
    show_name = ""
    extension = ""
    episode = ""  # episode of the file well formated -> 1x07

    debugging = False
    testing = False

    def __init__(self, files_path, file_name, testing, debugging):
        self.files_path = files_path
        self.file_name = file_name
        self.f_abs_original_path = os.path.join(files_path, self.file_name)
        self.testing = testing
        self.debugging = debugging

    def is_well_formated(self):
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

    def __rename(self):
        """
        __rename(self)
            Renames a file with a new name.
        """

        self.f_abs_new_path = os.path.join(self.files_path, self.file_name_new)

        if self.debugging:
            Messages.debug_msg("_Rename info:")
            Messages.debug_msg("\tself.f_abs_original_path: {0}".format(self.f_abs_original_path))
            Messages.debug_msg("\tself.f_abs_new_path: {0}".format(self.f_abs_new_path))
            Messages.debug_msg("\tself.file_name: {0}".format(self.file_name))
            Messages.debug_msg("\tself.file_name_new: {0}".format(self.file_name_new))
            Messages.debug_msg("\tself.extension: {0}".format(self.extension))
            Messages.debug_msg("\tself.show_name {0}".format(self.show_name))
            Messages.debug_msg("\tself.episode: {0}".format(self.episode))
            Messages.debug_msg("\tself.ov: {0}".format(self.ov))

        if self.testing:
            self.__print_move()

        FilesHandler.mv(self.f_abs_original_path, self.f_abs_new_path,
                        self.debugging, self.testing)

    def __print_move(self):
        """
        __print_move(self)
        Displays the original file name and the new file name.
        """

        if self.file_name != self.file_name_new:
            Messages.mv_msg(self.file_name, self.file_name_new)

    def __translate(self):
        """
         __translate(self)
            Translates some series names.
        """

        name = self.show_name

        if name in TRANSLATED_NAMES:
            translated_name = TRANSLATED_NAMES.get(name)
            self.file_name_new = self.file_name_new.replace(name,
                                                            translated_name)
