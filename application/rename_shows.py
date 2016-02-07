#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        rename_shows.py
@interpreter: python3
"""

from crosscutting.condition_messages import print_info
from domain.subtitle import Subtitle
from domain.video import Video


def rename_subtitles(subtitles, path, testing):
    renamed_subtitles = False

    for subtitle in sorted(subtitles):
        current_subtitle = Subtitle(path, subtitle, testing)

        if current_subtitle.file_name != current_subtitle.new_file_name:
            renamed_subtitles = True

    if not renamed_subtitles:
        print_info("No subtitles renamed")


def rename_videos(videos, path, testing):
    renamed_videos = False

    for video in sorted(videos):
        current_video = Video(path, video, testing)

        if current_video.new_file_name and (current_video.file_name != current_video.new_file_name):
            renamed_videos = True

    if not renamed_videos:
        print_info("No videos renamed")
