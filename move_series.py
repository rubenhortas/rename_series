#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    move_series.py
"""

import argparse
import signal
import time

from application.move_series import move
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.constants import BUFFER_DISKS
from crosscutting.constants import FINAL_DISKS
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from presentation.utils.screen import clear_screen


if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        buffer_disks_mounted = False
        final_disks_mounted = False
        input_dest = None

        parser = argparse.ArgumentParser(description="Move some series.")

        parser.add_argument(
            'path', metavar='path', nargs=1, help='path to move files')

        parser.add_argument("-t", "--test", dest="test",
                            action="store_true",
                            help="Runs a single test showing the output.")

        args = parser.parse_args()
        testing = args.test
        user_path = args.path

        clear_screen()

        if user_path:
            is_buffer = False

            if os.path.isdir(user_path):
                if user_path in BUFFER_DISKS:
                    is_buffer = True

                move(user_path, is_buffer, testing)
            else:
                print_error("{0} is not a directory.".format(input_dest))

        else:
            buffer_disks_mounted = get_mounted_disks(BUFFER_DISKS)
            final_disks_mounted = get_mounted_disks(FINAL_DISKS)

            if (not buffer_disks_mounted == [] or not final_disks_mounted == []):
                pass

                for disk in buffer_disks_mounted:
                    move(disk, True, testing)

                for disk in final_disks_mounted:
                    move(disk, False, testing)

            else:
                print_error("No mounted disks found.")

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
