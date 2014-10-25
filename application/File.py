#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      File.py
"""

import os
from presentation import Messages


class File:
    """
    Class File
            Superclass that stores data and operations common
            to child classes videofile and subtitlefile.
    """

    files_path = ''
    f_abs_original_path = ''  # Absolute orignal file path
    f_abs_new_path = ''
    file_name = ''
    file_name_new = ''
    show_name = ''
    extension = ''
    episode = ''  # episode of the file well formated -> 1x07

    debugging = False
    testing = False

    def __init__(self, files_path, file_name, testing, debugging):
        self.file_name = file_name
        self.f_abs_original_path = os.path.join(files_path, self.file_name)
        self.__remove_quality()
        self.testing = testing
        self.debugging = debugging

    def __rename(self):
        """
        __rename(self)
            Renames a file with a new name.
        """

        if (not self.testing) and (not self.debugging):
            try:
                os.rename(self.f_abs_original_path, self.f_abs_new_path)
            except IOError as e:
                Messages.error_msg(e)

        if self.debugging:
            Messages.debug_msg('_Rename info:')
            Messages.debug_msg('\tself.f_abs_original_path: %s'
                               % self.f_abs_original_path)
            Messages.debug_msg('\tself.f_abs_new_path: %s'
                               % self.f_abs_new_path)
            Messages.debug_msg('\tself.file_name: %s' % self.file_name)
            Messages.debug_msg('\tself.file_name_new: %s' % self.file_name_new)
            Messages.debug_msg('\tself.extension: %s' % self.extension)
            Messages.debug_msg('\tself.show_name %s' % self.show_name)
            Messages.debug_msg('\tself.episode: %s' % self.episode)
            Messages.debug_msg('\tself.ov: %s' % self.ov)

        if self.testing:
            self.__print_move()

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

        translated_names = {
            'Family Guy':   'Padre de familia',
            'Marvels Agents of S H I E L D': 'Marvel\'s Agents Of S.H.I.E.L.D.',
            'Supernatural': 'Sobrenatural',
            'The Simpsons': 'Los Simpson',
            'Warehouse 13': 'Almacén 13',
            'Warehouse13': 'Almacén 13'
        }

        if name in translated_names:
            translated_name = translated_names.get(name)
            self.file_name_new = self.file_name_new.replace(name, translated_name)

    def __remove_quality(self):
        """
        __remove_quality(self)
            Removes video quality from file
        """

        if '720p' in self.file_name:
            self.file_name = self.file_name.replace('720p', '')
        elif '1080p' in self.file_name:
            self.file_name = self.file_name.replace('1080p', '')

        self.file_name = self.file_name.replace('..', '.')
        self.file_name = self.file_name.strip()

