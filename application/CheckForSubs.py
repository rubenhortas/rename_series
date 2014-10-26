#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    CheckForSubs.py
"""

import os
import re

from presentation import Messages


def check_for_subs(l_videos, l_subtitles, current_path, debugging, testing):

    subtitles_found = False

    Messages.info_msg("Checking for subs in {0}".format(current_path))

    for video in l_videos:
        if debugging:
            Messages.debug_msg("check_for_subs:")
            Messages.debug_msg("\tvideo: {0}".format(video))

        if "(VO)" in video:
            video_name = os.path.splitext(video)[0]
            video_extension = os.path.splitext(video)[1]

            name_pattern = re.compile("^[\w \(\)]*", re.UNICODE)

            video_match = name_pattern.search(video_name)

            if video_match:
                video_name_clean = video_match.group(0)

                if "(VO)" in video_name_clean:
                    video_name_clean = video_name_clean.replace("(VO)", "")

                video_name_clean = video_name_clean.strip()

            for subtitle in l_subtitles:
                if debugging:
                    Messages.debug_msg("\tsub: {0}".format(subtitle))

                subtitle_name = os.path.splitext(subtitle)[0]

                subtitle_match = name_pattern.search(subtitle_name)

                if subtitle_match:
                    subtitle_name_clean = subtitle_match.group(0)
                    subtitle_name_clean = subtitle_name_clean.strip()

                    if debugging:
                        Messages.debug_msg("\t\tvideo: {0} vs sub: {1}".format(video_name_clean, subtitle_name_clean))

                    if video_name_clean == subtitle_name_clean:
                        subtitles_found = True

                        new_video_name = subtitle_name + video_extension
                        l_subtitles.remove(subtitle)

                        Messages.mv_msg(video, new_video_name)

                        if (not testing and not debugging):
                            try:
                                current_video_path = os.path.join(current_path,
                                                                  video)
                                new_video_path = os.path.join(current_path,
                                                              new_video_name)
                                os.rename(current_video_path, new_video_path)
                            except IOError as ex:
                                Messages.error_msg(ex)
                                print()
                        break

    if not subtitles_found:
        print("Subtitles not found")
        print()
