#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        constants.py
@interpreter: python3
"""

# FILE_WELL_FORMATED_PATTERN = re.compile(
#     "(?P<season>[\d]{1,2})x(?P<episode>[\d]{1,2})(?P<episode_title>[\w \-\(\)])?\.(?P<extension>[\w]{3})", re.UNICODE)

REQUIRED_PYTHON_VERSION = 3

# rename_series configuration
DIR_SEASON_NAME = "Temporada"
SHOWS_PATHS = ['/home/ruben/Vídeos', '/home/ruben/Vídeos/temp']


# File extensions
DEFAULT_SUBTITLE_EXTENSION = ".srt"
SUBTITLE_EXTENSIONS = [".srt"]
VIDEO_EXTENSIONS = [".mp4", ".avi", ".mkv"]

# Translations
TRANSLATED_NAMES = {
    "Family Guy": "Padre de familia",
    "Marvels Agents of S H I E L D": "Marvel\"s Agents Of S.H.I.E.L.D.",
    "Supernatural": "Sobrenatural",
    "The Simpsons": "Los Simpson",
    "Warehouse 13": "Almacén 13",
    "Warehouse13": "Almacén 13"
}

# Subtitles VOS
VOS = {
    "(Español (España))": "VOSE",
    "(Español (Latinoamérica))": "VOSE"
}
