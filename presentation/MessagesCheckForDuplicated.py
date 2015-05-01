#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    MessagesCheckForDuplicated
"""

from .Color import Color
from .Tag import Tag


def header(path, debugging, testing):
    """
    Header()
        Print a couple of introduction lines
    """

    header_msg = Tag.info + "Checking for duplicate files in " + \
        Color.bold_red + path

    if not debugging and not testing:
        print(header_msg)
    else:
        header_msg_testing = header_msg + " [TEST]" + Color.end + "\n"
        print(header_msg_testing)


def bestFile_msg(f):
    """
    bestFile_msg(f):
        Prints best file choosen.
    Arguments:
        - f: File choosen.
    """

    print("\tBest file: " + Color.bold_green + f + Color.end)


def repeatedFile_msg(f):
    """
    bestFile_msg(f):
        Prints best file choosen.
    Arguments:
        - f: File choosen.
    """

    print(Color.bold_yellow + f + Color.end + " duplicated")


def rm_msg(f):
    """
    rm_msg(f)
        Prints a message indicating a file to remove.
    Arguments:
        - f: (string) File to remove.
    """

    rm_msg = "Deleting " + Color.bold_red + f + Color.end
