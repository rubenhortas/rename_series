#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    messages_move_series.py
"""

from presentation.color import Color
from presentation.tag import Tag


def print_header(current_disk, testing):
    """
    print_header()
        Print a couple of introduction lines

    Args:
        testing:
        current_disk:
    """

    header = "{0} Moving files to {1}{2}{3}".format(
        Tag.info, Color.bold_red, current_disk, Color.end)

    if testing:
        header = "{0} {1}[TEST]{2}".format(
            header, Color.bold_red, Color.end)

    print(header)


def print_mv(orig, dest):
    """
    print_mv(msg)
        Prints a message indicating the original file dest_path (or name)
        and its destiny dest_path (or name).
    Arguments:
        orig: (string) Original file dest_path/name.
        dest: (string) Destiny file dest_path/name.
    """

    print("{0} -> {1}{2}{3}".format(orig, Color.bold_green, dest, Color.end))
