#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    file_handler.py
"""

import os

from crosscutting.condition_messages import print_error
from crosscutting.constants import SUBTITLE_EXTENSIONS
from crosscutting.constants import VIDEO_EXTENSIONS
from crosscutting.messages_move_series import print_mv


def is_video(f):
    file_extension = os.path.splitext(f)[1]
    if file_extension in VIDEO_EXTENSIONS:
        return True
    else:
        return False


def is_subtitle(f):
    file_extension = os.path.splitext(f)[1]
    if file_extension in SUBTITLE_EXTENSIONS:
        return True
    else:
        return False


def get_videos(path):
    """
    get_videos(path)
        Gets video files from a directory.
    Arguments:
        path: (string) Path.
    """

    videos = []

    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if is_video(f):
                videos.append(f)

    return videos


def get_subtitles(path):
    """
    get_subtitles(path)
        Gets subtitle files from a directory.
    Arguments:
        path: (string) Path.
    """

    subtitles = []

    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if is_subtitle(f):
                subtitles.append(f)

    return subtitles


def mv(orig, dest, testing):
    """
    mv(orig, dest, debugging, testing)
        Moves all the files to the same directory.
    Arguments:
        orig: (string) Directory where the files will be gotten.
        dest: (string) Directory where the files will be moved.
        testing: (boolean) Indicates if the program is in testing mode.s
    """

    try:
        orig_file_name = os.path.basename(orig)
        dest_file_name = os.path.basename(dest)

        print_mv(orig_file_name, dest_file_name)

        if not testing:
            os.rename(orig, dest)
    except Exception as ex:
        print_error(ex)
