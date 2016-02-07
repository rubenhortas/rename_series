#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    rename_shows.py
"""

import argparse
import os
import signal

from application.rename_shows import rename_subtitles
from application.rename_shows import rename_videos
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from crosscutting.constants import SHOWS_PATHS
from crosscutting.messages_rename_series import print_header
from domain.utils.file_handler import get_subtitles
from domain.utils.file_handler import get_videos
from presentation.utils.screen import clear_screen

if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        videos = []
        subtitles = []
        directories_found = False

        parser = argparse.ArgumentParser(description='Renames some series.')

        parser.add_argument('paths', metavar='paths', nargs='*', help='paths to rename files')

        parser.add_argument('-t', '--test', dest='testing', action='store_true',help='run a single test showing the expected output')

        args = parser.parse_args()

        testing = args.testing

        clear_screen()

        if args.paths:
            paths = args.paths
        else:
            paths = SHOWS_PATHS

        for current_path in paths:
            if not os.path.isdir(current_path):
                print_error('{0} is not a directory'.format(current_path))
            else:
                directories_found = True

                print_header(current_path, testing)

                subtitles = get_subtitles(current_path)
                videos = get_videos(current_path)

                rename_subtitles(subtitles, current_path, args.testing)
                rename_videos(videos, current_path, args.testing)

        if not directories_found:
            print_error('Has not entered any directory')

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
