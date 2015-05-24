#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    MessagesSearchForDuplicated
"""

from .Color import Color
from .Tag import Tag


def header(path, debugging, testing):
    """
    header()
        Print a couple of introduction lines
    """

    header_msg = "{0}Checking for duplicate files in {1}{2}{3}".format(Tag.info, Color.bold_red, path, Color.end)

    if(debugging or testing):
        header_msg = "{0} {1}[TEST]{2}".format(header_msg, Color.bold_red, Color.end)


def bestFile_msg(f):
    """
    bestFile_msg(f):
        Prints best file choosen.
    Arguments:
        - f: File choosen.
    """

    print("\tBest file: {0}{1}{2}".format(Color.bold_green, f, Color.end))


def repeatedFile_msg(f):
    """
    bestFile_msg(f):
        Prints repeated file found.
    Arguments:
        - f: File choosen.
    """

    print("{0}{1}{2} duplicated".format(Color.bold_yellow, f, Color.end))


def rm_msg(f):
    """
    rm_msg(f)
        Prints a message indicating a file to remove.
    Arguments:
        - f: (string) File to remove.
    """

    msg = "Deleting {0}{1}{2}".format(Color.bold_red, f, Color.end)
    print(msg)
