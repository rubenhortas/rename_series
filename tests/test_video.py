#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        test_video.py
@interpreter: python3
"""

import unittest

from crosscutting import constants
from domain.video import Video

"""
$ python3 -m unittest tests/test_subtitle.py 
"""


class TestVideo(unittest.TestCase):
    path = None
    video_name = None
    testing = None

    def setUp(self):
        self.path = "/home/user/testpath/"
        self.testing = True

    def test_remove_quality(self):
        for quality in constants.QUALITIES:
            self.video_name = "testVideo101{0}.mkv".format(quality)
            expected = "testVideo101.mkv"

            video = Video(self.path, self.video_name, self.testing)
            video.file_name = self.video_name
            video._remove_quality()

            self.assertEqual(expected, video.file_name)

    def test_get_episode_1(self):
        self.video_name = "Show 1x20.mp4"
        expected = "1x20"

        video = Video(self.path, self.video_name, self.testing)
        video.file_name = self.video_name
        video._set_episode()

        self.assertEqual(expected, video.episode_in_file_name)
        self.assertEqual(expected, video.episode)
        self.assertEqual(self.video_name, video.new_file_name)

    def test_get_episode_2(self):
        self.video_name = "Show S01E20.mp4"
        expected_episode = "1x20"
        expected_episode_in_name = "S01E20"
        expected_video_new_file_name = "Show 1x20.mp4"

        video = Video(self.path, self.video_name, self.testing)
        video.file_name = self.video_name
        video._set_episode()

        self.assertEqual(expected_episode, "1x20")
        self.assertEqual(expected_episode_in_name, video.episode_in_file_name)
        self.assertEqual(expected_video_new_file_name, video.new_file_name)

    def test_get_episode_3(self):
        self.video_name = "Show [Cap.120].mp4"
        expected_episode = "1x20"
        expected_episode_in_name = "[Cap.120]"
        expected_new_file_name = "Show 1x20.mp4"

        video = Video(self.path, self.video_name, self.testing)
        video.file_name = self.video_name
        video._set_episode()

        self.assertEqual(expected_episode, "1x20")
        self.assertEqual(expected_episode_in_name, video.episode_in_file_name)
        self.assertEqual(expected_new_file_name, video.new_file_name)

    def test_get_episode_4(self):
        self.video_name = "Show 120.mp4"
        expected_episode = "1x20"
        expected_episode_in_name = "120"
        expected_new_file_name = "Show 1x20.mp4"

        video = Video(self.path, self.video_name, self.testing)
        video.file_name = self.video_name
        video._set_episode()

        self.assertEqual(expected_episode, video.episode)
        self.assertEqual(expected_episode_in_name, video.episode_in_file_name)
        self.assertEqual(expected_new_file_name, video.new_file_name)

    def test_get_episode_year(self):
        self.video_name = "Movie 2015.mkv"

        video = Video(self.path, self.video_name, self.testing)
        video.file_name = self.video_name
        video._set_episode()

        self.assertIsNone(video.episode)
        self.assertIsNone(video.episode_in_file_name)
        self.assertIsNone(video.new_file_name)

    def test_is_serie_true(self):
        self.video_name = "Show S1E20.mp4"

        video = Video(self.path, self.video_name, self.testing)

        self.assertTrue(video.is_show())

    def test_is_serie_false(self):
        self.video_name = "Movie 20015.mkv"

        video = Video(self.path, self.video_name, self.testing)

        self.assertFalse(video.is_show())

    def test_set_ov_true(self):
        self.video_name = "Show S1E20 [www.kat.cr].mp4"

        video = Video(self.path, self.video_name, self.testing)
        video._set_ov()

        self.assertTrue(video.original_version)

    def test_set_ov_false(self):
        self.video_name = "Show S1E20.mp4"

        video = Video(self.path, self.video_name, self.testing)
        video._set_ov()

        self.assertFalse(video.original_version)

    def test_get_show_name_shows(self):
        self.video_name = "VideoName S1E01.mp4"
        expected = "VideoName"

        video = Video(self.path, self.video_name, self.testing)
        video._set_show_name()

        self.assertEqual(expected, video.show_name)

        self.video_name = "VideoName.blah.blah.S1E01.mp4"
        expected = "VideoName blah blah"

        video = Video(self.path, self.video_name, self.testing)
        video._set_show_name()

        self.assertEqual(expected, video.show_name)

    def test_get_show_name_movies(self):
        self.video_name = "VideoName.blah.blah.(2015).mp4"
        expected = "VideoName blah blah (2015)"

        video = Video(self.path, self.video_name, self.testing)
        video._set_show_name()

        self.assertEqual(expected, video.show_name)

    def test_wrap_year_1(self):
        self.video_name = "VideoName (2015).mp4"
        expected = self.video_name

        video = Video(self.path, self.video_name, self.testing)
        output = video._wrap_year(self.video_name)

        self.assertEqual(expected, output)

    def test_wrap_year_2(self):
        self.video_name = "VideoName 2015.mp4"
        expected = "VideoName (2015).mp4"

        video = Video(self.path, self.video_name, self.testing)
        output = video._wrap_year(self.video_name)

        self.assertEqual(expected, output)

    def test_expand_show_name(self):
        self.video_name = "americanhstory S1E01.mp4"
        expected = "American Horror Story"

        video = Video(self.path, self.video_name, self.testing)
        video.show_name = "americanhstory"
        video._expand_show_name()

        self.assertEqual(expected, video.show_name)

    def test_get_episode_title(self):
        self.video_name = "VideoName S1E01 great title.mp4"
        expected = "great title"

        video = Video(self.path, self.video_name, self.testing)

        self.assertEqual(expected, video.episode_title)

    def test_get_new_file_name(self):
        self.video_name = "VideoName (2015) S1E01 great title.mp4"
        expected = "VideoName (2015) 1x01 great title.mp4"

        video = Video(self.path, self.video_name, self.testing)

        self.assertEqual(expected, video.new_file_name)


if __name__ == "__main__":
    unittest.main()
