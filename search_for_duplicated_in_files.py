#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      /home/ruben/workspace/git/rename_series/look_for_duplicated_in_files.py
"""

import argparse
import os
import signal
import sys

from application.search_for_duplicated_in_files import search_in_file
from application.search_for_duplicated_in_files import search_in_files
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from crosscutting.messages_search_for_duplicated_in_files import print_header
from presentation.utils.clear_screen import clear_screen


if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        in_file = ""
        from_file = ""

        parser = argparse.ArgumentParser(
            description='Look for repeated strings in file[s]')
        parser.add_argument('-from', dest='from_file',
                            help="from file")
        parser.add_argument('-in', dest='in_file',
                            help="in file")
        parser.add_argument("-t", "--test", dest="test",
                            action="store_true",
                            help="runs a single test showing the expected output")

        args = parser.parse_args()

        if args.in_file:
            if os.path.isfile(args.in_file):
                in_file = args.in_file

                clear_screen()

                print_header(in_file, args.from_file, args.test)

                if args.from_file:

                    if os.path.isfile(args.from_file):
                        from_file = args.from_file

                        search_in_files(in_file, from_file)

                    else:
                        error_msg("{0} is not a file.".format(args.from_file))
                        sys.exit(-1)
                else:
                    search_in_file(in_file)

            else:
                error_msg("{0} is not a file.".format(args.in_file))
                sys.exit(-1)
    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
