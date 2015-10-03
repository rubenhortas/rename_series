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
import os
import time

from application.utils import ListHandler
from application.utils.ListHandler import print_list
from application.utils.TimeHandler import print_time
from crosscutting.Messages import error_msg
from domain.DestDir import DestDir
from domain.File import File
from domain.utils.FileHandler import get_files, mv
from presentation.MessagesMoveSeries import header
from presentation.utils.ClearScreen import clear_screen


path_movies_local = "/home/ruben/Lab/fakedVideos"
buffer_disks = ["/home/ruben/Lab/fakedDestBuffer"]
final_disks = ["/home/ruben/Lab/fakedDest"]


def __move_to_known_disks(disks_list, is_buffer, debugging, testing):
    """
    __move_to_known_disks(disks_list, is_buffer, debugging, testing)
        Move the series to the known disks for store tv shows.
    Arguments:
        - disks_list: (string list) List with the disks used to store shows.
        - is_buffer: (boolean) Indicates if the disk is a disk buffer or not.
        - debugging: (boolean) Indicates if the program is in debug mode.
        - testing: (boolean) Indicates if the program is in testing mode.s
    """

    disks_found = False

    for disk in disks_list:
        if os.path.isdir(disk):
            disks_found = True
            __start_moving(disk, is_buffer, debugging, testing)
        else:
            error_msg("{0} is not a directory".format(disk))

    return disks_found


def __start_moving(dest, is_buffer, debugging, testing):
    """
    __start_moving(dest, is_buffer, debugging, testing)
        Move the series to the known disks for store tv shows.
    Arguments:
        - dest: (string list) Destiny directories.
        - is_buffer: (boolean) Indicates if the disk is a disk buffer or not.
        - debugging: (boolean) Indicates if the program is in debug mode.
        - testing: (boolean) Indicates if the program is in testing mode.
    """

    nonexistent_paths = []

    header(dest, debugging, testing)

    list_files = sorted(get_files(path_movies_local, debugging))

    if(debugging):
        print("Files in {0}".format(dest))
        print_list(list_files)

    for f in list_files:
        this_file = File(path_movies_local, f, testing, debugging)
        if(this_file.is_well_formated()
           and ('(English)' not in f)):

            if(is_buffer):
                # If is a buffer disk: Bulk move
                final_dest = os.path.join(dest, this_file.file_name)
                mv(this_file.f_abs_original_path, final_dest, debugging,
                   testing)

            else:
                file_dest = DestDir(f, dest, debugging, testing)

                if(file_dest.final_dest is not None):
                    mv(this_file.f_abs_original_path, file_dest.final_dest,
                       debugging, testing)
                else:
                    nonexistent_dest = os.path.join(dest, file_dest.show_name)
                    nonexistent_paths = ListHandler.append(nonexistent_dest,
                                                           nonexistent_paths)

    for path in nonexistent_paths:
        error_msg("{0} does not exist.".format(path))

    print()


if __name__ == "__main__":

    python_required_version = 2

    check_python_version(python_required_version)

    signal.signal(signal.SIGINT, signal_handler)

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

    parser.add_argument("-d", "--debug", dest="debug",
                        action="store_true",
                        help="Shows debug info")

    args = parser.parse_args()

    testing = args.test
    debugging = args.debug
    input_dest = args.input_dest

    clear_screen()

    # If user specifies a directory to move the files
    if input_dest:
            if(os.path.isdir(input_dest)):
                time_ini = time.clock()
                __start_moving(input_dest, False, debugging, testing)
                time_fin = time.clock()
                total_time = time_fin - time_ini
                print_time(total_time)
            else:
                error_msg("{0} is not a directory.".format(input_dest))

    # If the user did not specify a directory, search for known mounted disks
    else:
        time_ini = time.clock()
        buffer_disks_found = __move_to_known_disks(buffer_disks, True,
                                                   debugging, testing)
        final_disks_found = __move_to_known_disks(final_disks, False,
                                                  debugging, testing)
        time_fin = time.clock()

        if not buffer_disks_found and not final_disks_found:
            error_msg("No disks found.")
        else:
            total_time = time_fin - time_ini
            print_time(total_time)
