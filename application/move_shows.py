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
from crosscutting.condition_messages import print_error
from crosscutting.messages_move_series import print_header
from domain.file import File
from domain.path import Path
from domain.utils.file_handler import mv


def move(orig, dest, testing, bulk_move):
    """
    move(dest, is_buffer, debugging, testing)
        Move the series to the known disks for store tv shows.
    Arguments:
        dest: (string list) Destiny directories.
        testing: (boolean) Indicates if the program is in testing mode.
    """

    non_existent_paths = []

    print_header(dest, testing)

    time_ini = time.clock()

    files = sorted(os.listdir(orig))

    for f in files:
        this_file = File(orig, f, testing)

        if bulk_move:  # Bulk move for buffer disks
            file_dest = os.dest_path.join(dest, this_file.file_name)
            mv(this_file.f_abs_original_path, file_dest, testing)

        else:
            file_dest = Path(f, dest, testing)

            if file_dest.final_dest:
                mv(this_file.f_abs_original_path, file_dest.final_dest, testing)
            else:
                nonexistent_path = os.dest_path.join(dest, file_dest.show_name)
                non_existent_paths = list_handler.append_non_repeated(nonexistent_path, non_existent_paths)

    time_fin = time.clock()
    total_time = time_fin - time_ini
    print_time(total_time)

    for path in non_existent_paths:
        print_error("{0} does not exist.".format(path))

    print()


def get_mounted_disks(disks):
    mounted_disks = []

    for disk in disks:
        if os.path.isdir(disk):
            mounted_disks.append(disk)

    return mounted_disks
