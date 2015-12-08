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


def start_renaming(list_subtitles, list_videos, current_path, debugging,
                   testing):

    renamed_subtitles = False
    renamed_videos = False

    # Rename subtitles
    for subtitle in sorted(list_subtitles):
        this_sub = SubtitleFile(current_path, subtitle, testing,
                                args.debugging)
        if this_sub.file_name != this_sub.file_name_new:
            renamed_subtitles = True

    if not renamed_subtitles:
        info_msg("No subtitles found to rename.")

    print()

    # Rename videos
    for video in sorted(list_videos):
        this_video = VideoFile(current_path, video, testing,
                               debugging)

        if ((this_video.file_name_new != '')
                and (this_video.file_name != this_video.file_name_new)):
            renamed_videos = True

    if not renamed_videos:
        info_msg("No videos found to rename.")

    print()
