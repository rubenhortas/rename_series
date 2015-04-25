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
from presentation import MessagesRenameSeries
from utils.ClearScreen import clear_screen
from utils.FileHandler import get_files_separated


def __start_renaming(list_subtitles, list_videos, current_path):

    renamed_subtitles = False
    renamed_videos = False

    # Rename subtitles
    for subtitle in sorted(list_subtitles):
        this_sub = SubtitleFile(current_path, subtitle, testing,
                                debugging)
        if this_sub.file_name != this_sub.file_name_new:
            renamed_subtitles = True

    if not renamed_subtitles:
        Messages.info_msg("No subtitles found to rename.")

    print()

    # Rename videos
    for video in sorted(list_videos):
        this_video = VideoFile(current_path, video, testing,
                               debugging)

        if ((this_video.file_name_new != '')
                and (this_video.file_name != this_video.file_name_new)):
            renamed_videos = True

    if not renamed_videos:
        Messages.info_msg("No videos found to rename.")

    print()


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
    parser.add_argument('-d', '--debug', dest='debug', action='store_true',
                        help='Shows debug info')
    parser.add_argument('-D', '--dir', dest='user_dir',
                        help='Uses only the specified directory/path.')

    args = parser.parse_args()
    testing = args.test
    debugging = args.debug
    user_dir = args.user_dir

    clear_screen()

    if(user_dir):
        valid_dirs = True
        MessagesRenameSeries.Header(user_dir, debugging, testing)

        list_videos, list_subtitles = get_files_separated(user_dir, debugging)
        __start_renaming(list_subtitles, list_videos, user_dir)

        # Check for subs
        l_videos, l_subs = get_files_separated(user_dir, debugging)
        check_for_subs(l_videos, l_subs, user_dir, debugging, testing)

    else:
        for current_path in shows_paths:
            if not os.path.isdir(current_path):
                Messages.error_msg('%s is not a directory' % current_path)
            else:
                valid_dirs = True

                MessagesRenameSeries.Header(current_path, debugging, testing)

                list_videos, list_subtitles = get_files_separated(current_path,
                                                                  debugging)
                __start_renaming(list_subtitles, list_videos, current_path)

                # Check for subtitles
                l_videos, l_subs = get_files_separated(current_path, debugging)
                check_for_subs(l_videos, l_subs, current_path, debugging,
                               testing)

    if not valid_dirs:
        Messages.error_msg('Has not entered any directory')
