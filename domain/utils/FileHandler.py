#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Files.py
"""

import os

from crosscutting.constants import VIDEO_EXTENSIONS


def is_video(file):
    file_extension = os.path.splitext(file)[1]
    if file_extension in VIDEO_EXTENSIONS:
        return True
    else:
        return False


def is_subtitle(file):
    file_extension = os.path.splittext(file)[1]
    if file_extension == ".srt":
        return True
    else:
        return False


def get_files(directory, debugging):
    """
    __get_files(directory)
        Gets video and subtitle files from a directory.
    """

    list_files = []

    try:
        files_in_d = os.listdir(directory)

        for f in files_in_d:
            if os.path.isfile(os.path.join(directory, f)):  # Skip directories
                # Exclude another types than videos or subtitles
                if is_video(f) or __is_subtitle(f):
                    list_files.append(f)

        if debugging:
            print("+ get_files()")
            print_list(list_files)

    except Exception as ex:
        Messages.exception_msg(ex)

    return list_files


def get_videos(path, debugging):
    """
    get_videos(path)
        Gets video files from a directory.
    Arguments:
        - path: (string) Path.
    """

    videos = []

    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if is_video(f):
                videos.append(f)

    return videos


def get_subtitles(path, debugging):
    """
    get_subtitles(path)
        Gets subtitle files from a directory.
    Arguments:
        - path: (string) Path.
    """

    subtitles = []

    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if is_subtitle(f):
                subtitles.append(f)

    return subtitles


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

    MessagesMoveSeries.mv_msg(orig, dest)

    if not testing and not debugging:
        try:
            os.rename(orig, dest)
        except Exception as ex:
            Messages.error_msg(ex)
