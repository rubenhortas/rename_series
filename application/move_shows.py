#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        move_shows.py
@interpreter: python3
"""

import os
import time

from application.utils import list_handler
from application.utils.time_handler import print_time
from config import FINAL_DISKS
from config import SHOWS_PATHS
from crosscutting.condition_messages import print_error, print_info
from crosscutting.messages_move_series import print_header
from domain.file import File
from domain.path import Path
from domain.utils.file_handler import mv


def move(dests, testing):
    """
    move(dest, bulk_move, debugging, testing)
        Move the series to the known disks for store tv shows.
    Arguments:
        dests: (string list) Destiny directories.
        testing: (boolean) Indicates if the program is in testing mode.
    """

    files_moved = False
    non_existent_paths = []

    time_ini = time.clock()

    for show_path in SHOWS_PATHS:
        for dest in dests:
            print_header(dest, testing)
            if os.path.isdir(show_path):
                files = os.listdir(show_path)

                for f in files:
                    this_file = File(show_path, f)

                    if this_file.is_well_formatted():
                        files_moved = True
                        if dest not in FINAL_DISKS:
                            file_dest = os.path.join(dest, this_file.file_name)
                            mv(this_file.original_path, file_dest, testing)

                        else:
                            file_dest = Path(f, dest, testing)

                            if file_dest.final_dest:
                                mv(this_file.original_path, file_dest.final_dest, testing)
                            else:
                                nonexistent_path = os.path.join(show_path, file_dest.show_name)
                                non_existent_paths = list_handler.append_non_repeated(nonexistent_path,
                                                                                      non_existent_paths)
            else:
                print_error("{0} is not a valid path.".format(show_path))

    if files_moved:
        for path in non_existent_paths:
            print_info("\n\n{0} does not exist.".format(path))

        time_fin = time.clock()
        total_time = time_fin - time_ini
        print_time(total_time)
    else:
        print_info("No files moved.")


def get_mounted_disks(disks):
    mounted_disks = []

    for disk in disks:
        if os.path.isdir(disk):
            mounted_disks.append(disk)

    return mounted_disks
