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
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from presentation.utils.screen import clear_screen


buffer_disks = []
final_disks = []


def __start_moving(dest, is_buffer, testing):
    print("TODO")


def move_to_known_disks(disks_list, is_buffer, testing):
    print("TODO")

if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        buffer_disks_found = False
        final_disks_found = False
        input_dest = None
        time_ini = 0

        parser = argparse.ArgumentParser(description="Move some series.")

        parser.add_argument("-D", "--dest", dest="input_dest",
                            help="Directory where the series will be moved.")

        parser.add_argument("-t", "--test", dest="test",
                            action="store_true",
                            help="Runs a single test showing the output.")

        args = parser.parse_args()

        testing = args.test
        input_dest = args.input_dest

        clear_screen()

        # If user specifies a directory to move the files
        if input_dest:
            if os.path.isdir(input_dest):
                time_ini = time.clock()
                start_moving(input_dest, False, testing)
                time_fin = time.clock()
                total_time = time_fin - time_ini
                print_time(total_time)
            else:
                print_error("{0} is not a directory.".format(input_dest))

        # If the user did not specify a directory, search for known mounted
        # disks
        else:
            time_ini = time.clock()
            buffer_disks_found = move_to_known_disks(buffer_disks, True,
                                                     testing)
            final_disks_found = move_to_known_disks(final_disks, False,
                                                    testing)
            time_fin = time.clock()

            if not buffer_disks_found and not final_disks_found:
                print_error("No disks found.")
            else:
                total_time = time_fin - time_ini
                print_time(total_time)

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
