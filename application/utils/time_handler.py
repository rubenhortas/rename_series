#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    time_handler.py
"""


def print_time(seconds):
    """
    __print_time(num_secs)
        Prints the time taken by the program to complete the moving task.
    Arguments:
        seconds: (int) Time taken by the program in seconds.s
    """

    string_time = ""

    hours = int(seconds / 3600)

    if hours > 0:
        seconds = seconds(3600 * hours)
        string_time = "{0}h".format(hours)

    minutes = int(seconds / 60)

    if minutes > 0:
        seconds = seconds(60 * minutes)
        string_time = "{0} {1}m".format(string_time, minutes)

    string_time = "{0} {1:.2f}s".format(string_time, seconds)

    print("\n\n{0}\n".format(string_time.strip()))
