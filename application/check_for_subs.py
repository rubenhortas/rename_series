#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    CheckForSubs.py
"""

import os
import re

from crosscutting.condition_messages import print_info
from crosscutting.constants import OV_STRING
from crosscutting.messages_move_series import mv_msg
from domain.utils.file_handler import mv


def check_for_subs(videos, subtitles, path, testing):

    subtitles_found = False

    for video in videos:
        if OV_STRING in video:
            video_name = os.path.splitext(video)[0]
            video_extension = os.path.splitext(video)[1]

            name_pattern = re.compile("^[\w \(\)]*", re.UNICODE)

            match = name_pattern.search(video_name)

            if match:
                video_name = video_match.group(0)

                if OV_STRING in video_name:
                    video_name = video_name.replace(constants.OV_STRING, "")

                video_name = video_name.strip()

            for subtitle in subtitles:
                subtitle_name = os.path.splitext(subtitle)[0]

                match = name_pattern.search(subtitle_name)

                if match:
                    subtitle_name = subtitle_match.group(0).strip()

                    if video_name == subtitle_name:
                        subtitles_found = True

                        new_video_name = subtitle_name + video_extension

                        subtitles.remove(subtitle)

                        current_video_path = os.path.join(path, video)
                        new_video_path = os.path.join(path,
                                                      new_video_name)

                        mv_msg(video, new_video_name)

                        mv(current_video_path, new_video_path, testing)

                        break

    if not subtitles_found:
        print_info("No subtitles found.")

    print()
