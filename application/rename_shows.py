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
import os
import re

from config import OV_STRING
from crosscutting.condition_messages import print_info
from domain.subtitle import Subtitle
from domain.utils.file_handler import mv
from domain.video import Video


def rename_subtitles(subtitles, path, testing):
    renamed_subtitles = False

    for subtitle in subtitles:
        current_subtitle = Subtitle(path, subtitle, testing)

        if current_subtitle.new_file_name and (current_subtitle.file_name != current_subtitle.new_file_name):
            renamed_subtitles = True

    if not renamed_subtitles:
        print_info("No subtitles renamed")


def rename_videos(videos, path, testing):
    renamed_videos = False

    for video in videos:
        current_video = Video(path, video, testing)

        if current_video.new_file_name and (current_video.file_name != current_video.new_file_name):
            renamed_videos = True

    if not renamed_videos:
        print_info("No videos renamed")


def check_for_subtitles(videos, subtitles, path, testing):
    name_pattern = re.compile("^[\w \(\)]*", re.UNICODE)
    subtitles_found = False

    print_info("Checking for subtitles")

    for video in videos:
        if OV_STRING in video:
            match = name_pattern.search(video)

            if match:
                video_name = match.group(0)
                video_name = video_name.replace(OV_STRING, "")
                video_name = video_name.strip()
                video_extension = os.path.splitext(video)[1]

                for subtitle in subtitles:
                    subtitle_original_name = os.path.splitext(subtitle)[0]

                    match = name_pattern.search(subtitle_original_name)

                    if match:
                        subtitle_name = match.group(0).strip()

                        if video_name == subtitle_name:
                            subtitles_found = True
                            new_video_name = subtitle_original_name + video_extension

                            subtitles.remove(subtitle)

                            current_video_path = os.path.join(path, video)
                            new_video_path = os.path.join(path, new_video_name)

                            mv(current_video_path, new_video_path, testing)

                            break

    if not subtitles_found:
        print_info("No subtitles found.\n")
