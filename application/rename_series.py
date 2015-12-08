#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        rename_series.py
@interpreter: python3
"""

from crosscutting.condition_messages import print_info
from domain import subtitle


def rename_subtitles(subtitles, path, testing, debugging):
    renamed_subtitles = False

    for subtitle in sorted(subtitles):
        current_subtitle = subtitle(path, subtitle, testing, debugging)

        if current_subtitle.file_name != current_subtitle.new_file_name:
            renamed_subtitles = True

    if not renamed_subtitles:
        print_info("No subtitles renamed")


def rename_videos(videos, path, testing, debugging):
    renamed_videos = False

    for video in sorted(videos):
        current_video = video(path, current_video, testing, debugging)

        if ((this_video.file_name_new != '')
                and (this_video.file_name != this_video.file_name_new)):
            # TODO: Change empty string for a None type
            renamed_videos = True

    if not renamed_videos:
        print_info("No videos renamed")
