#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    messages_search_for_duplicated_episodes.py
"""

from presentation.color import Color
from presentation.tag import Tag


def header(path, testing):
    """
    header()
        Print a couple of introduction lines
    """

    header_msg = "{0}Checking for duplicate files in {1}{2}{3}".format(
        Tag.info, Color.bold_red, path, Color.end)

    if not testing:
        print(header_msg)
    else:
        header_msg = "{0} {1}[TEST]{2}".format(
            header_msg, Color.bold_red, Color.end)


def best_file_msg(f):
    """
    best_file_msg(f):
        Prints best file choosen.
    Arguments:
        - f: File choosen.
    """

    print("\tBest file: {0}{1}{2}".format(Color.bold_green, f, Color.end))


def repeated_file_msg(f):
    """
    repeated_file_msg(f):
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

    print("Deleting {0}{1}{2}".format(Color.bold_red, f, Color.end))
