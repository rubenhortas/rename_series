#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Files.py
"""

import os

from presentation import Messages
from .ListsHandlers import print_list


def __is_subtitle(current_file):
    ext = os.path.splitext(current_file)[1]
    if ext == ".srt":
        return True
    else:
        return False


def __is_video(current_file):
    ext = os.path.splitext(current_file)[1]
    video_formats = [".mp4", ".avi", ".mkv"]
    if ext in video_formats:
        return True
    else:
        return False


def get_files(directory, debugging):
    """
    __get_files(directory)
        Gets video and subtitle files from a directory.
    """

    list_files = []

    files_in_d = os.listdir(directory)

    for f in files_in_d:
        if os.path.isfile(os.path.join(directory, f)):  # Skip directories
            # Exclude another types than videos or subtitles
            if __is_video(f) or __is_subtitle(f):
                list_files.append(f)

    if debugging:
        print("+ get_files()")
        print_list(list_files)

    return list_files


def get_files_separated(directory, debugging):
    """
    __get_files_separated(directory)
        Gets files from a directory and separates them in videos or subtitles.
    """

    list_videos = []
    list_subtitles = []

    files_in_d = os.listdir(directory)

    for f in files_in_d:
        if os.path.isfile(os.path.join(directory, f)):  # Skip directories
            # Exclude another types than videos or subtitles
            if __is_video(f):
                list_videos.append(f)
            elif __is_subtitle(f):
                list_subtitles.append(f)

    if debugging:
        print("+ get_files_separated()")
        print_list(list_videos)
        print_list(list_subtitles)

    return list_videos, list_subtitles


def mv(orig, dest, debugging, testing):
    """
    mv(orig, dest, debugging, testing)
        Moves all the files to the same directory.
    Arguments:
        - orig: (string) Directory where the files will be gotten.
        - dest: (string) Directory where the files will be moved.
        - debugging: (boolean) Indicates if the program is in debug mode.
        - testing: (boolean) Indicates if the program is in testing mode.s
    """

    Messages.mv_msg(orig, dest)

    if not testing and not debugging:
        try:
            os.rename(orig, dest)
        except IOError as ex:
            Messages.error_msg(ex)
