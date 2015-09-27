#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Messages.py
"""

from presentation.Color import Color
from presentation.Tag import Tag


def error_msg(msg):
    """
    error_msg(msg)
        Prints an error message.
    Arguments:
        - msg: (string) Error message.
    """

    print("{0} {1}".format(Tag.error, msg))


def warning_msg(msg):
    """
    warning_msg(msg)
        Prints a warning message.
    Arguments:
        - msg: (string) Warning message.
    """

    print("{0} {1}".format(Tag.warning, msg))


def info_msg(msg):
    """
    info_msg(msg)
        Prints an information message.
    Arguments:
        - msg: (string) Information message.
    """

    print("{0} {1}".format(Tag.info, msg))


def debug_msg(msg):
    """
    debug_msg(msg)
        Prints a debug message.
    Arguments:
        - msg: (string) Debug message.
    """

    print("{0} {1}".format(Tag.debug, msg))


def exception_msg(msg):
    """
    exception_msg(msg)
        Prints an exception message.
    Arguments:
        - msg: (string) System exception message.
    """

    print("{0} {1}".format(Tag.ex, msg))
