#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      /home/ruben/workspace/git/rename_series/look_for_duplicated_in_files.py
"""

import argparse
import difflib
import os
import re
import string
import sys

from presentation.Messages import error_msg
from presentation.MessagesSearchForDuplicatedInFiles import header, duplicated_msg
from utils.ClearScreen import clear_screen


MATCH_THRESHOLD = 0.90


def __get_match_ratio(e1, e2):
    """
    __get_match_ratio(str1, str2)
        Compares two lines.
    Arguments:
        - e1: (line) element one.
        - e2: (line) element two.
    """

    # Normalizartion
    str1 = e1.lower().strip()
    str2 = e2.lower().strip()

    for p in string.punctuation:
        str1.replace(p, '')
        str2.replace(p, '')

    # Replace multiple spaces for one space
    str1 = re.sub('\s+', str1, ' ')
    str2 = re.sub('\s+', str2, ' ')

    # Get match ratio
    match_ratio = difflib.SequenceMatcher(None, str1, str2).ratio()

    return match_ratio


def __get_file_list(file_name):
    """
    __get_file_list(file_name)
        Gets file content as list
    Arguments:
        - file_name: (string) File [path and] name.
    """

    l_file = []

    f = open(file_name)

    for line in f:
        l_file.append(line)

    f.close()

    return sorted(l_file)


def __compare_lists_items(l1, l2, in_file, from_file):
    """
    __compare_lists_items(l1, l2, from_file)
        Searchs if exists every element of l1 in l2
    Arguments:
        - l1: (list) List one.
        - l2: (list) List two.
        - from_file: (string) File wich contains l2 items.
    """

    for e1 in l1:
        matches = 0
        for e2 in l2:
            match_ratio = __get_match_ratio(e1, e2)
            if(match_ratio > MATCH_THRESHOLD):
                matches = matches + 1
                if(from_file or (matches > 1)):
                    duplicated_msg(e1.strip(), e2.strip(), in_file, from_file, round((match_ratio * 100), 2))
                    l2.remove(e2)


def __search_in_files(in_file, from_file):
    """
    __search_in_files(in_file, from_file)
        Searchs for coincidences between two files.
        Searchs in file 'in_file' coincidences from file 'from_file'.
    Arguments:
        - in_file: (string) File [path and] name.
        - from_file: (string) File [path and] name.
    """

    l_in_file = __get_file_list(in_file)
    l_from_file = __get_file_list(from_file)

    __compare_lists_items(l_in_file, l_from_file, in_file, from_file)


def __search_in_file(in_file):
    """
    __search_in_file(in_file)
        Searchs for coincidences inside a file.
    Arguments:
        - in_file: (string) File [path and] name.
    """

    l_in_file = __get_file_list(in_file)

    l_in_file_tmp = l_in_file[:]

    __compare_lists_items(l_in_file, l_in_file_tmp, in_file, None)


if __name__ == '__main__':

    in_file = ""
    from_file = ""

    parser = argparse.ArgumentParser(description='Look for repeated strings in file[s]')
    parser.add_argument('-from', dest='from_file',
                        help="from file")
    parser.add_argument('-in', dest='in_file',
                        help="in file")
    parser.add_argument("-t", "--test", dest="test",
                        action="store_true",
                        help="runs a single test showing the expected output")

    parser.add_argument("-d", "--debug", dest="debug",
                        action="store_true",
                        help="show debug info")

    args = parser.parse_args()

    if(args.in_file):
        if(os.path.isfile(args.in_file)):
            in_file = args.in_file

        if(in_file):  # in_file is a file

            clear_screen()

            header(in_file, args.from_file, args.debug, args.test)

            if(args.from_file):  # from_file especified

                if(os.path.isfile(args.from_file)):
                    from_file = args.from_file

                if(from_file):  # from_file is a file
                    __search_in_files(in_file, from_file)

                else:  # from_file is not a file
                    error_msg("{0} is not a file.".format(args.from_file))
                    sys.exit(-1)

            else:  # from_file not especified
                __search_in_file(in_file)

        else:  # in_file is not a file
            error_msg("{0} is not a file.".format(args.in_file))
            sys.exit(-1)
