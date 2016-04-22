#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        search_for_duplicated_in_files.py
@interpreter: python3
"""

import difflib
import re
import string

from application.utils.dictionary_utils import increment
from crosscutting.messages_search_for_duplicated_in_files import print_duplicated_msg
from domain.duplicated_item import DuplicatedItem
from domain.match import Match

MATCH_THRESHOLD = 0.90


def search_in_files(in_file, from_file):
    """
    search_in_files(in_file, from_file)
        Searches for coincidences between two files.
        Searches in file 'in_file' coincidences from file 'from_file'.
    Arguments:
        in_file: (string) File [dest_path and] name.
        from_file: (string) File [dest_path and] name.
    """

    in_file_content = __get_file_content(in_file)
    from_file_content = __get_file_content(from_file)

    __compare_lists_items(from_file_content, in_file_content, from_file, in_file)


def search_in_file(in_file):
    """
    search_in_file(in_file)
        Searches for coincidences inside a file.
    Arguments:
        in_file: (string) File [dest_path and] name.
    """

    in_file_content = __get_file_content(in_file)

    in_file_content_tmp = in_file_content[:]  # Deep copy

    __compare_lists_items(in_file_content, in_file_content_tmp, in_file, None)


def __get_file_content(file_name):
    """
    __get_file_content(file_name)
        Gets file content as a sorted list. One list item per line.
    Arguments:
        file_name: (string) File [dest_path and] name.
    """

    file_content = []

    f = open(file_name, encoding="UTF-8", errors="ignore")

    for line in f:
        file_content.append(line.strip())

    f.close()

    return sorted(file_content)


# noinspection PyUnusedLocal
def __compare_lists_items(list1, list2, in_file, from_file):
    """
    __compare_lists_items(list1, list2, from_file)
        Searches if exists every element of list1 in list2
    Arguments:
        list1: (list) List one.
        list2: (list) List two.
        from_file: (string) File containing list2 items.
    """

    duplicated_items = {}
    possible_matches = {}

    for item_list1 in list1:
        possible_matches = {}
        for item_list2 in list2:
            match_ratio = __get_match_ratio(item_list1, item_list2)
            if match_ratio > MATCH_THRESHOLD:
                match = Match(item_list2, match_ratio * 100)
                increment(possible_matches, match)
                matches = possible_matches[match]

        if matches > 1:
            duplicated_item = DuplicatedItem(item_list1, possible_matches)
            duplicated_items[duplicated_item] = matches

    __print_duplicated_items(duplicated_items)


def __get_match_ratio(item1, item2):
    """
    __get_match_ratio(str1, str2)
        Compares two lines.
    Arguments:
        item1: (line) item one.
        item2: (line) item two.
    """

    str1 = item1.lower().strip()
    str2 = item2.lower().strip()

    for p in string.punctuation:
        str1.replace(p, '')
        str2.replace(p, '')

    # Replace multiple spaces for one space
    str1 = re.sub('\s+', str1, ' ')
    str2 = re.sub('\s+', str2, ' ')

    match_ratio = difflib.SequenceMatcher(None, str1, str2).ratio()

    return match_ratio


def __print_duplicated_items(duplicated_items):
    for item in duplicated_items:
        original_item = item.name

        for possible_match in item.possible_matches:
            duplicated_match_ratio = possible_match.match_ratio
            duplicated_times = item.possible_matches[possible_match]

            print_duplicated_msg(original_item, duplicated_match_ratio, duplicated_times)
