#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    rename_series.py
"""

import argparse
import os

from application.CheckForSubs import check_for_subs
from application.SubtitleFile import SubtitleFile
from application.VideoFile import VideoFile
from presentation import Messages
from utils import ListsHandlers
from utils.ClearScreen import clear_screen


def __get_files(directory):
    """
    __get_files(directory)
        Gets files from directory and separates them in videos or subtitles
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
        print('+ Get_files()')
        ListsHandlers.print_list(list_videos)
        ListsHandlers.print_list(list_subtitles)

    return list_videos, list_subtitles


def __is_subtitle(current_file):
    ext = os.path.splitext(current_file)[1]
    if ext == '.srt':
        return True
    else:
        return False


def __is_video(current_file):
    ext = os.path.splitext(current_file)[1]
    video_formats = ['.mp4', '.avi', '.mkv']
    if ext in video_formats:
        return True
    else:
        return False


def __start_renaming(list_subtitles, list_videos):

    renamed_subtitles = False
    renamed_videos = False

    # Rename subtitles
    for subtitle in list_subtitles:
        this_sub = SubtitleFile(current_path, subtitle, testing,
                                debugging)
        if this_sub.file_name != this_sub.file_name_new:
            renamed_subtitles = True

    if not renamed_subtitles:
        print('No subtitles found to rename.')

    # Rename videos
    for video in list_videos:
        this_video = VideoFile(current_path, video, testing,
                               debugging)

        if ((this_video.file_name_new != '')
                and (this_video.file_name != this_video.file_name_new)):
            renamed_videos = True

    if not renamed_videos:
        print('No videos found to rename.')


if __name__ == '__main__':

    # Absolute paths containing tv shows
    shows_paths = ['/home/ruben/peliculas', '/home/ruben/peliculas/temp']

    list_videos = []
    list_subtitles = []
    valid_dirs = False

    # Parse console arguments
    parser = argparse.ArgumentParser(description='Rename some series.')
    parser.add_argument('-t', '--test', dest='test', action='store_true',
                        help='Runs a single test showing the output.')
    parser.add_argument('-D', '--debug', dest='debug', action='store_true',
                        help='Shows debug info')
    parser.add_argument('-d', '--dir', dest='user_dir', action='store_true',
                        help='Uses only the specified directory/path.')

    args = parser.parse_args()
    testing = args.test
    debugging = args.debug
    user_dir = args.user_dir

    clear_screen()

    if(user_dir):
        Messages.Header(user_dir, debugging, testing)
        list_videos, list_subtitles = __get_files(user_dir)
        __start_renaming(list_subtitles, list_videos)

        # Check for subs
        l_videos, l_subs = __get_files(user_dir)
        check_for_subs(l_videos, l_subs, user_dir, debugging, testing)

    else:
        for current_path in shows_paths:
            if not os.path.isdir(current_path):
                Messages.error_msg('%s is not a directory' % current_path)
            else:
                valid_dirs = True

                Messages.Header(current_path, debugging, testing)
                list_videos, list_subtitles = __get_files(current_path)
                __start_renaming(list_subtitles, list_videos)
                print()

                # Check for subs
                l_videos, l_subs = __get_files(current_path)
                check_for_subs(l_videos, l_subs, current_path, debugging,
                               testing)

    if not valid_dirs:
        Messages.error_msg('Has not entered any directory')
