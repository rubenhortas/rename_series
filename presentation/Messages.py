#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Messages.py
"""

from .Color import Color
from .Tag import Tag


def error_msg(msg):
    """
    error_msg(msg)
        Prints an error message.
    Arguments:
        - msg: (string) Error message.
    """

    print(Tag.error + msg)


def warning_msg(msg):
    """
    warning_msg(msg)
        Prints a warning message.
    Arguments:
        - msg: (string) Warning message.
    """

    print(Tag.warning + msg)


def info_msg(msg):
    """
    info_msg(msg)
        Prints an information message.
    Arguments:
        - msg: (string) Information message.
    """

    print(Tag.info + msg)


def debug_msg(msg):
    """
    debug_msg(msg)
        Prints a debug message.
    Arguments:
        - msg: (string) Debug message.
    """

    print(Tag.debug + str(msg))


def exception_msg(msg):
    """
    exception_msg(msg)
        Prints an exception message.
    Arguments:
        - msg: (string) System exception message.
    """

    print(Tag.ex + str(msg))


def Append(msg, l):
    """
    Append(msg, l)
        Appends a message to a list if it not exists.
    Arguments:
        - msg: (msg) Message.
        - l: (list) List of messages.
    """

    if msg not in l:
        l.append(msg)


def mv_msg(orig, dest):
    """
    mv_msg(msg)
        Prints a message indicating the original file path (or name)
        and its destiny path (or name).
    Arguments:
        - orig: (string) Original file path/name.
        - dest: (string) Destiny file path/name.
    """

    mv_msg = orig + " -> " + Color.bold_green + dest + Color.end
    print(mv_msg)


def rm_msg(f):
    """
    rm_msg(f)
        Prints a message indicating a file to remove.
    Arguments:
        - f: (string) File to remove.
    """

    rm_msg = "Deleting " + Color.bold_red + f + Color.end
