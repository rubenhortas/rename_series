#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    search_for_duplicated_episodes.py
"""

import argparse
import signal

from application.search_for_duplicated_episodes import search_duplicated_episodes
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from crosscutting.messages_search_for_duplicated_episodes import print_header
from presentation.utils.screen import clear_screen

if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        parser = argparse.ArgumentParser(
            description='Look for repeated chapters')

        parser.add_argument('dest_path', metavar='dest_path',
                            help="dest_path where the files are being sought")

        parser.add_argument("-t", "--test", dest="testing",
                            action="store_true",
                            help="run a single test showing the expected output")

        parser.add_argument("-d", "--debug", dest="debugging",
                            action="store_true",
                            help="show debug info")

        args = parser.parse_args()

        clear_screen()

        print_header(args.path, args.testing)

        search_duplicated_episodes(args.path, args.testing)

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
