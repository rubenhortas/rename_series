#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    list_handler.py
"""


def print_list(l):
    """
    print_list(l)
        Prints a list in a nice format.
    Args:
        - l : (string list) List to print.
    """

    for element in l:
        print(element)


def append(obj, l):
    """
    append(object, list)
        Appends an object to a list, if not already included.
    Args:
        - obj : (object) Object to append.
        - l : (list) List to append the object.
    """

    if obj not in l:
        l.append(obj)

    return l
