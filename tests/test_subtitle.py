#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        test_subtitle.py
@interpreter: python3
"""

import unittest

from domain.subtitle import Subtitle

"""
$ python3 -m unittest tests/test_subtitle.py 
"""


class TestSubtitle(unittest.TestCase):
    path = None
    file_name = None
    testing = None

    def setUp(self):
        self.path = "/home/user/testpath/"
        self.testing = True

    def test_set_new_name_espanol_espana_ok(self):
        self.file_name = "Subtitle 0x00 (Español (España)).srt"
        expected = "Subtitle 0x00 VOSE.srt"
        sub = Subtitle(self.path, self.file_name, self.testing)
        self.assertEqual(sub.new_file_name, expected)

    def test_set_new_name_espanol_latinoamerica_ok(self):
        self.file_name = "Subtitle 0x00 (Español (Latinoamérica)).srt"
        expected = "Subtitle 0x00 VOSE.srt"
        sub = Subtitle(self.path, self.file_name, self.testing)
        self.assertEqual(sub.new_file_name, expected)

    def test_set_new_name_fail(self):
        self.file_name = "Subtitle 0x00.srt"
        sub = Subtitle(self.path, self.file_name, self.testing)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
