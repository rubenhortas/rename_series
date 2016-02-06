#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        test_episode.py
@interpreter: python3
"""

import unittest

from domain.episode import Episode

"""
$ python3 -m unittest tests/test_file.py 
"""


class TestFile(unittest.TestCase):
    # noinspection PyUnusedLocal,PyUnresolvedReferences
    def test_get_format_1_ok(self):
        file_name = "Show 1x20.mp4"
        expected = "1x20"

        episode = Episode(file_name)
        episode_in_file_name = None
        episode_formatted = None

        episode._Episode__get_ep_format_1(file_name)

        self.assertEqual(expected, episode.episode_in_file_name)
        self.assertEqual(expected, episode.episode_formatted)

    # noinspection PyUnusedLocal,PyUnresolvedReferences
    def test_get_format_2_ok(self):
        file_name = "Show S1E20.mp4"
        expected_episode_in_file_name = "S1E20"
        expected_episode_formatted = "1x20"

        episode = Episode(file_name)
        episode_in_file_name = None
        episode_formatted = None

        episode._Episode__get_ep_format_2(file_name)

        self.assertEqual(expected_episode_in_file_name, episode.episode_in_file_name)
        self.assertEqual(expected_episode_formatted, episode.episode_formatted)

    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnresolvedReferences
    def test_get_format_3_ok(self):
        file_name = "Show [Cap.120].mp4"
        expected_episode_in_file_name = "[Cap.120]"
        expected_episode_formatted = "1x20"

        episode = Episode(file_name)
        episode_in_file_name = None
        episode_formatted = None

        episode._Episode__get_ep_format_3(file_name)

        self.assertEqual(expected_episode_in_file_name, episode.episode_in_file_name)
        self.assertEqual(expected_episode_formatted, episode.episode_formatted)

    # noinspection PyUnusedLocal,PyUnresolvedReferences,PyUnresolvedReferences
    def test_get_format_4_ok(self):
        file_name = "Show120.mp4"
        expected_episode_in_file_name = "120"
        expected_episode_formatted = "1x20"

        episode = Episode(file_name)
        episode_in_file_name = None
        episode_formatted = None

        episode._Episode__get_ep_format_4(file_name)

        self.assertEqual(expected_episode_in_file_name, episode.episode_in_file_name)
        self.assertEqual(expected_episode_formatted, episode.episode_formatted)

        file_name = "Show120.mp4"
        expected_episode_in_file_name = "120"
        expected_episode_formatted = "1x20"

        episode = Episode(file_name)
        episode_in_file_name = None
        episode_formatted = None

        episode._Episode__get_ep_format_4(file_name)

        self.assertEqual(expected_episode_in_file_name, episode.episode_in_file_name)
        self.assertEqual(expected_episode_formatted, episode.episode_formatted)


if __name__ == "__main__":
    unittest.main()
