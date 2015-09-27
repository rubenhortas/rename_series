#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    MessagesMoveSeries.py
"""

from presentation.Color import Color
from presentation.Tag import Tag


def header(current_disk, debugging, testing):
    """
    header()
        Print a couple of introduction lines
    """

    header_msg = "{0} Moving files to {1}{2}{3}".format(Tag.info, Color.bold_red, current_disk, Color.end)

    if(debugging or testing):
        header_msg = "{0} {1}[TEST]{2}".format(header_msg, Color.bold_red, Color.end)
    print(header_msg)

def mv_msg(orig, dest):
    """
    mv_msg(msg)
        Prints a message indicating the original file path (or name)
        and its destiny path (or name).
    Arguments:
        - orig: (string) Original file path/name.
        - dest: (string) Destiny file path/name.
    """

    mv_msg = "{0} -> {1}{2}{3}".format(orig, Color.bold_green, dest, Color.end)
    print(mv_msg)
