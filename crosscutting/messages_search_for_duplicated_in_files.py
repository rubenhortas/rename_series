#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      messages_search_for_duplicated_in_files.py
"""

from presentation.color import Color
from presentation.tag import Tag


def header(in_file, from_file, testing):
    """
    header()
        Print a couple of introduction lines
    """

    if not from_file:
        header_msg = "{0} Checking for duplicate files in {1} {2} {3}".format(
            Tag.info, Color.bold_green, in_file, Color.end)
    else:
        header_msg = "{0} Checking for duplicate files from {1} {2} {3} in {4} {5} {6}".format(
            Tag.info, Color.bold_green, from_file, Color.end, Color.bold_green, in_file, Color.end)

    if not testing:
        print(header_msg)
    else:
        print("{0} [TEST] {1}".format(header_msg, Color.end))


def duplicated_msg(in_item, from_item, in_file, from_file, match_ratio):
    """
    duplicated(in_file, from_file)
        Prints duplicated item found.
    """

    if not from_file:
        if match_ratio == 100:
            print("* \"{0}{1}{2}\" found (\"{4}{5}{6}\" {8}{9}% match{10})".format(Color.bold_yellow, in_item, Color.end,
                                                                                   in_file, Color.bold_green, from_item, Color.end, from_file, Color.bold_red, match_ratio, Color.end))
        else:
            print("* \"{0}{1}{2}\" possible match (\"{4}{5}{6}\" {8}{9}%{10} similar)".format(Color.bold_yellow, in_item,
                                                                                              Color.end, in_file, Color.bold_green, from_item, Color.end, from_file, Color.bold_yellow, match_ratio, Color.end))

    else:
        if match_ratio == 100:
            print("* \"{0}{1}{2}\" in {3} found in {7} (\"{4}{5}{6}\" {8}{9}% match{10})".format(Color.bold_yellow, in_item,
                                                                                                 Color.end, in_file, Color.bold_green, from_item, Color.end, from_file, Color.bold_red, match_ratio, Color.end))
        else:
            print("* \"{0}{1}{2}\" in {3} possible match in {7} (\"{4}{5}{6}\" {8}{9}%{10} similar)".format(Color.bold_yellow, in_item,
                                                                                                            Color.end, in_file, Color.bold_green, from_item, Color.end, from_file, Color.bold_yellow, match_ratio, Color.end))
