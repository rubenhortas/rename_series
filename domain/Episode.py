#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Episode.py
"""

import re


PAT1 = re.compile("[0-9]{1,2}x[0-9]{1,2}")
PAT2 = re.compile("S[0-9]{1,2}E[0-9]{1,2}")
PAT3 = re.compile("\[Cap.[0-9]*\]")
PAT4 = re.compile("[0-9]{3,5}")


class Episode():

    episode_in_name = None
    episode = None

    def __init__(self, file_name):

        ep = None
        episode_in_name = None

        # Format 1x20
        episode_match = PAT1.search(file_name)
        if episode_match:
            episode_in_name = episode_match.group(0)
            ep = episode_in_name

        else:  # Format S01E20 or S1E20
            episode_match = PAT2.search(file_name)
            if episode_match:
                episode_in_name = episode_match.group(0)
                ep = self.__get_ep_format_1(episode_in_name)

            else:  # Format [Cap.120]
                episode_match = PAT3.search(file_name)
                if episode_match:
                    episode_in_name = episode_match.group(0)
                    ep = self.__get_ep_format_2(episode_in_name)
                    ep = self.__get_ep_format_3(ep)

                else:  # Format 120
                    episode_match = PAT4.search(file_name)
                    if episode_match:
                        episode_in_name = episode_match.group(0)
                        # Check the length
                        # In series like Warehouse13415, the title
                        # is pasted to the season and episode (4x15)
                        if len(episode_in_name) > 4:
                            episode_in_name = episode_in_name[2:]

                        ep = self.__get_ep_format_3(episode_in_name)
        self.episode = ep
        self.episode_in_name = episode_in_name

    def __get_ep_format_1(self, episode_orig):  # Formats S01E20, S1E20

        episode = episode_orig

        if "S0" in episode:
            episode = episode.replace("S0", "")

        else:  # If only "S" is in episode
            episode = episode.replace("S", "")

        episode = episode.replace("E", "x")

        return episode

    def __get_ep_format_2(self, episode_orig):  # Format [Cap.120]

        episode = episode_orig.replace("[Cap.", "")
        episode = episode.replace("]", "")

        return episode

    def __get_ep_format_3(self, episode_orig):  # Format 120

        episode_num = episode_orig[-2:]
        season_num = episode_orig[:-2]

        episode = "{0}x{1}".format(season_num, episode_num)

        return episode
