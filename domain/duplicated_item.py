#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        dupicated_item.py
@interpreter: python3
"""


class DuplicatedItem():
    name = None
    match_ratio = 0

    def __init__(self, name, match_ratio):
        self.name = name
        self.match_ratio = match_ratio

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name