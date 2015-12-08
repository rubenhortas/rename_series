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

from application.utils.PythonUtils import exit_signal_handler
from application.utils.PythonUtils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from crosscutting.constants import SHOWS_PATHS
from crosscutting.messages_rename_series import print_header


if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_signal_handler)

    if get_interpreter_version == REQUIRED_PYTHON_VERSION:

        list_videos = []
        list_subtitles = []
        valid_dirs = False

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
            print_header(args.user_dir, args.debugging, args.testing)

            list_videos, list_subtitles = get_files_separated(args.user_dir,
                                                              args.debugging)
            __start_renaming(list_subtitles, list_videos, args.user_dir,
                             args.debugging, args.testing)

            # Check for subs
            l_videos, l_subs = get_files_separated(
                args.user_dir, args.debugging)
            check_for_subs(l_videos, l_subs, args.user_dir, args.debugging,
                           args.testing)

        else:
            for current_path in shows_paths:
                if not os.path.isdir(current_path):
                    error_msg('{0} is not a directory'.format(current_path))
                else:
                    valid_dirs = True

                    print_header(current_path, args.debugging, args.testing)

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
            print_error('Has not entered any directory')

    else:
        print_error("Requires Python {0}".format(PYTHON_REQUIRED_VERSION))
        exit(0)
