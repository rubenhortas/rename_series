#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    rename_series.py
"""


import argparse
import os
import signal

from application.CheckForSubs import check_for_subs
from application.utils.PythonUtils import check_python_version
from application.utils.PythonUtils import signal_handler
from crosscutting.Messages import info_msg, error_msg
from crosscutting.MessagesRenameSeries import header
from domain.SubtitleFile import SubtitleFile
from domain.VideoFile import VideoFile
from domain.utils.FileHandler import get_files_separated
from presentation.utils.ClearScreen import clear_screen


def __start_renaming(list_subtitles, list_videos, current_path, debugging,
                     testing):

    renamed_subtitles = False
    renamed_videos = False

    # Rename subtitles
    for subtitle in sorted(list_subtitles):
        this_sub = SubtitleFile(current_path, subtitle, testing,
                                args.debugging)
        if this_sub.file_name != this_sub.file_name_new:
            renamed_subtitles = True

    if not renamed_subtitles:
        info_msg("No subtitles found to rename.")

    print()

    # Rename videos
    for video in sorted(list_videos):
        this_video = VideoFile(current_path, video, testing,
                               debugging)

        if ((this_video.file_name_new != '')
                and (this_video.file_name != this_video.file_name_new)):
            renamed_videos = True

    if not renamed_videos:
        info_msg("No videos found to rename.")

    print()


if __name__ == '__main__':

    required_python_version = 2

    check_python_version(required_python_version)

    signal.signal(signal.SIGINT, signal_handler)

    # Absolute paths containing tv shows
    shows_paths = ['/home/ruben/Vídeos', '/home/ruben/Vídeos/temp']

    list_videos = []
    list_subtitles = []
    valid_dirs = False

    # Parse console arguments
    parser = argparse.ArgumentParser(description='Renames some series.')
    parser.add_argument('-t', '--test', dest='testing', action='store_true',
                        help='run a single test showing the expected output')
    parser.add_argument('-d', '--debug', dest='debugging', action='store_true',
                        help='show debug info')
    parser.add_argument('-D', '--dir', dest='user_dir',
                        help='use only the specified directory/path')

    args = parser.parse_args()

    clear_screen()

    if(args.user_dir):
        valid_dirs = True
        header(args.user_dir, args.debugging, args.testing)

        list_videos, list_subtitles = get_files_separated(args.user_dir,
                                                          args.debugging)
        __start_renaming(list_subtitles, list_videos, args.user_dir,
                         args.debugging, args.testing)

        # Check for subs
        l_videos, l_subs = get_files_separated(args.user_dir, args.debugging)
        check_for_subs(l_videos, l_subs, args.user_dir, args.debugging,
                       args.testing)

    else:
        for current_path in shows_paths:
            if not os.path.isdir(current_path):
                error_msg('{0} is not a directory'.format(current_path))
            else:
                valid_dirs = True

                header(current_path, args.debugging, args.testing)

                list_videos, list_subtitles = get_files_separated(current_path,
                                                                  args.debugging)
                __start_renaming(list_subtitles, list_videos, current_path,
                                 args.debugging, args.testing)

                # Check for subtitles
                l_videos, l_subs = get_files_separated(current_path,
                                                       args.debugging)
                check_for_subs(l_videos, l_subs, current_path, args.debugging,
                               args.testing)

    if not valid_dirs:
        error_msg('Has not entered any directory')
