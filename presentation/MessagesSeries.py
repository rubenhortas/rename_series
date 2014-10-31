#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    MessagesSeries.py
"""

from Color import Color


def Header(current_path, debugging, testing):
    """
    Header()
        Print a couple of introduction lines
    """

    if debugging or testing:
        print("Renaming files in " + Color.bold + Color.red + current_path +
              " [TEST]" + Color.end + "\n")
    else:
        print("Renaming files in " + Color.bold + Color.red + current_path +
              Color.end + "\n")
