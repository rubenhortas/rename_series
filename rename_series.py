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

from application.rename_series import rename_subtitles
from application.rename_series import rename_videos
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from crosscutting.constants import SHOWS_PATHS
from crosscutting.messages_rename_series import print_header
from domain.utils.file_handler import get_subtitles
from domain.utils.file_handler import get_videos


if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        shows_paths = []
        videos = []
        subtitles = []
        directories_found = False

        parser = argparse.ArgumentParser(description='Renames some series.')
        parser.add_argument('-t', '--test', dest='testing', action='store_true',
                            help='run a single test showing the expected output')
        parser.add_argument('-p', '--path', dest='user_path',
                            help='use only the specified directory/path')

        args = parser.parse_args()

        clear_screen()

        if(args.user_path):
            shows_paths = shows_paths.append(args.user_dir)
        else:
            shows_paths = SHOWS_PATHS

        for current_path in shows_paths:
            if not os.path.isdir(current_path):
                print_error('{0} is not a directory'.format(current_path))
            else:
                directories_found = True

                print_header(current_path, args.testing)

                subtitles = get_subtitles(current_path)
                videos = get_videos(current_path)

                rename_subtitles(subtitles, path, args.testing)
                rename_videos(subtitles, path, args.testing)

#                 # Check for subtitles
#                 l_videos, l_subs = get_files_separated(current_path,
#                                                        args.debugging)
#                 check_for_subs(l_videos, l_subs, current_path, args.debugging,
#                                args.testing)

        if not directories_found:
            print_error('Has not entered any directory')

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
