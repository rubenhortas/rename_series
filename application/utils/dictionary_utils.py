#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        dictionary_utils.py
@interpreter: python3
"""


def increment(dictionary, key):
    if dictionary.get(key) is None:
        dictionary[key] = 0

    dictionary[key] = dictionary[key] + 1
