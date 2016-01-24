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
        - num_secs: (int) Time taken by the program in seconds.s
    """

    str_time = ""

    hrs = (num_secs / 3600)
    num_hrs = int(hrs)

    if num_hrs > 0:
        num_secs = num_secs - (3600 * hrs)
        str_time = str_time + str(num_hrs) + 'h '

    mins = (num_secs / 60)
    num_mins = int(mins)

    if num_mins > 0:
        num_secs = num_secs - (60 * mins)
        str_time = str_time + str(num_mins) + 'm '

    str_sec = '%2.2f' % num_secs
    str_time = str_time + str_sec + 's'

    print("*Time: %s" % str_time)
