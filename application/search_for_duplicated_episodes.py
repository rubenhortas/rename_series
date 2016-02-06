#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        search_for_duplicated_episodes.py
@interpreter: python3
"""

import os
import re

from crosscutting.condition_messages import print_exception
from crosscutting.constants import OV_STRING
from crosscutting.messages_search_for_duplicated_episodes import print_best_file
from crosscutting.messages_search_for_duplicated_episodes import print_no_repeated_found
from crosscutting.messages_search_for_duplicated_episodes import print_repeated_file
from crosscutting.messages_search_for_duplicated_episodes import print_rm
from domain.utils.file_handler import is_video

EPISODE_PATTERN = re.compile("[0-9]{1,2}x[0-9]{1,2}")


def search_duplicated_episodes(path, testing):
    repeated_episodes = []

    for root, dirs, files in os.walk(path, topdown=True, onerror=None, followlinks=False):

        if len(files) > 0:

            if len(dirs) == 0:
                episodes = []

                for f in files:
                    if is_video(f):
                        match = EPISODE_PATTERN.search(f)
                        if match:
                            episode = match.group(0)
                            if episode not in episodes:
                                episodes.append(episode)
                            else:
                                if episode not in repeated_episodes:
                                    repeated_episodes.append(episode)

        if repeated_episodes:
            __get_best_quality(root, repeated_episodes, testing)
        else:
            relative_path = root.replace(path, "")
            if relative_path is not "":  # skip root
                print_no_repeated_found(relative_path)


def __get_best_quality(path, repeated_episodes, testing):
    """
    __get_best_quality(path, episodes)
        Looking videos with best quality among the repeated videos.
    Arguments:
        - path: Current path for video files_in_path.
        - repeated_episodes: List of repeated episodes in the path.
    """

    files_in_path = []

    for f in os.listdir(path):
        file_absolute_path = os.path.join(path, f)
        if os.path.isfile(file_absolute_path):
            files_in_path.append(file_absolute_path)

    if files_in_path:
        for episode in repeated_episodes:

            relative_path = path.replace(path, "")
            print_repeated_file(os.path.join(relative_path, episode))

            best_file, discarted_files = __get_best_file(
                episode, files_in_path)

            print_best_file(best_file)

            for f in discarted_files:
                print_rm(f)

                if not testing:
                    try:
                        os.remove(f)
                    except Exception as e:
                        print_exception(e)


def __get_best_file(episode, files_in_path):
    """
    __get_best_file(episode, files_in_path)
        Gets the best file in the files_in_path.
        Returns best file and discarted files_in_path.
    Arguments:
        - episode: Current episode for search repeated files_in_path.
        - files_in_path: Files.
    """

    repeated_files = []
    best_file = None
    ov_file = None

    for f in files_in_path:
        if episode in f:
            if is_video(f):
                repeated_files.append(f)

    for f in repeated_files:

        if OV_STRING in f:
            ov_file = f
        else:
            if (best_file is None or
                        os.path.getsize(best_file) < os.path.getsize(f)):
                best_file = f

    if best_file is None:
        best_file = ov_file

    discarted_files = repeated_files[:]  # deep copy
    discarted_files.remove(best_file)

    return best_file, discarted_files
