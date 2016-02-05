#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        move_series.py
@interpreter: python3
"""

from application.utils.time_handler import print_time
from crosscutting.messages_move_series import print_header


# def __move_to_known_disks(disks_list, is_buffer, debugging, testing):
#     """
#     __move_to_known_disks(disks_list, is_buffer, debugging, testing)
#         Move the series to the known disks for store tv shows.
#     Arguments:
#         - disks_list: (string list) List with the disks used to store shows.
#         - is_buffer: (boolean) Indicates if the disk is a disk buffer or not.
#         - debugging: (boolean) Indicates if the program is in debug mode.
#         - testing: (boolean) Indicates if the program is in testing mode.s
#     """
#
#     disks_found = False
#
#     for disk in disks_list:
#         if os.path.isdir(disk):
#             disks_found = True
#             move(disk, is_buffer, debugging, testing)
#         else:
#             error_msg("{0} is not a directory".format(disk))
#
#     return disks_found
def move(dest, is_buffer, testing):
    """
    move(dest, is_buffer, debugging, testing)
        Move the series to the known disks for store tv shows.
    Arguments:
        - dest: (string list) Destiny directories.
        - is_buffer: (boolean) Indicates if the disk is a disk buffer or not.
        - testing: (boolean) Indicates if the program is in testing mode.
    """

    non_existent_paths = []

    header(dest, testing)

    time_ini = time.clock()

    list_files = sorted(get_files(path_movies_local))

#     for f in list_files:
#
#         this_file = File(path_movies_local, f, testing)
#
#         if(is_buffer):
#             # If is a buffer disk: Bulk move
#             final_dest = os.path.join(dest, this_file.file_name)
#             mv(this_file.f_abs_original_path, final_dest, testing)
#
#         else:
#             file_dest = DestDir(f, dest, debugging, testing)
#
#             if(file_dest.final_dest is not None):
#                 mv(this_file.f_abs_original_path, file_dest.final_dest,
#                    debugging, testing)
#             else:
#                 nonexistent_dest = os.path.join(dest, file_dest.show_name)
#                 non_existent_paths = ListHandler.append(nonexistent_dest,
#                                                         non_existent_paths)
    time_fin = time.clock()
    total_time = time_fin - time_ini
    print_time(total_time)

    for path in non_existent_paths:
        error_msg("{0} does not exist.".format(path))

    print()


def get_mounted_disks(disks):
    mounted_disks = []

    for disk in BUFFER_DISKS:
        if os.path.isdir(disk):
            mounted_disks.Append(disk)

    return mounted_disks
