#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    time_handler.py
"""


def print_time(num_secs):
    """
    __print_time(num_secs)
        Prints the time taken by the program to complete the moving task.
    Arguments:
        num_secs: (int) Time taken by the program in seconds.s
    """

    str_time = ""

    hrs = (num_secs / 3600)
    num_hrs = int(hrs)

    if num_hrs > 0:
        num_secs = num_secs(3600 * hrs)
        str_time = "{0}h".format(num_hrs)

    mins = (num_secs / 60)
    num_mins = int(mins)

    if num_mins > 0:
        num_secs = num_secs(60 * mins)
        str_time = "{0} {1}m".format(str_time, num_mins)

    str_sec = '%2.2f' % num_secs
    str_time = "{0} {1}s".format(str_time, str_sec)

    print("\n\n{0}\n".format(str_time.strip()))
