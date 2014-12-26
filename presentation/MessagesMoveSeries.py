#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    MessagesMoveSeries.py
"""

from .Color import Color
from .Tag import Tag


def Header(current_disk, debugging, testing):
    """
    Header()
        Print a couple of introduction lines
    """

    header_msg = Tag.info + "Moving files to " + Color.bold_red + current_disk

    if not debugging and not testing:
        print(header_msg)
    else:
        header_msg_testing = header_msg + " [TEST]" + Color.end + "\n"
        print(header_msg_testing)
