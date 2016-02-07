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

REQUIRED_PYTHON_VERSION = 3

# Application configuration
OV_STRING = "(VO)"

# rename_series configuration
SEASON_PATH_NAME = "Temporada"
# SHOWS_PATHS = ["/home/ruben/Vídeos", "/home/ruben/Vídeos/temp"]
SHOWS_PATHS = ["/home/ruben/Workspaces/temp/rename_series"]
BUFFER_DISKS = ["/home/ruben/Lab/fakedDestBuffer"]
FINAL_DISKS = ["/media/ruben/3tb"]

# File extensions
SUBTITLE_EXTENSIONS = [".srt"]
VIDEO_EXTENSIONS = [".mp4", ".avi", ".mkv"]

# Video qualities
QUALITIES = ["720p", "1080p"]

OWN_LANGUAGE_TRACKERS = ["[www.DivxTotaL.com]", "www.newpct1.com", "(Elitetorrent.net)"]

# Original Version name trackers
OV_TRACKERS = ["kat.cr", "[ettv]", "TASTETV", "[MPup]", "X264-DIMENSION"]

# Translations
TRANSLATED_NAMES = {
    "Family Guy": "Padre de familia",
    "Supernatural": "Sobrenatural",
    "The Simpsons": "Los Simpson",
    "Warehouse 13": "Almacén 13",
    "Warehouse13": "Almacén 13"
}

# Subtitles OV
OV_SUBTITLES = {
    "(Español (España))": "VOSE",
    "(Español (Latinoamérica))": "VOSE"
}

# Video Expanded Names
EXPANDED_NAMES = {
    # American Horror Story
    "americanhstory": "American Horror Story",
    "ahs": "American Horror Story",
    "americanstory": "American Horror Story",

    # Arrow
    "arr": "Arrow",

    # Bates Motel
    "bmotel": "Bates Motel",
    "bamotel": "Bates Motel",
    "batesmotel": "Bates Motel",

    # Boardwalk Empire
    "booardempire": "Boardwalk Empire",
    "boardwalkempire": "Boardwalk Empire",
    "boarempire": "Boardwalk Empire",

    # Bob"s Burgers
    "bobs burgers": "Bob\"s Burgers",

    # Castle
    "cas": "Castle",

    # Doctor Who
    "doctor who (2005)": "Doctor Who (2005)",
    "doctorwho": "Doctor Who (2005)",

    # Érase una vez
    "erasevez": "Érase una vez (Once upon a time)",
    "erase una vez": "Érase una vez (Once upon a time)",

    # El mentalista
    "ementalista": "El mentalista",
    "mentalista": "El mentalista",

    # Elementary
    "ele": "Elementary",
    "elem": "Elementary",
    "eleme": "Elementary",
    "elmntry": "Elementary",
    "elementary": "Elementary",

    # Marvel"s Agents of SHIELD
    "marvels agents of shield": "Marvel\"s Agents of S.H.I.E.L.D.",
    "marvels agents": "Marvel\"s Agents of S.H.I.E.L.D.",

    # Ray Donovan
    "rdonovan": "Ray Donovan",

    # South Park
    "sp": "South Park",
    "spark": "South Park",
    "southpark": "South Park",

    # Supernatural
    "supernatural": "Supernatural",

    # The Big Bang Theory
    "tbbtheory": "The Big Bang Theory",
    "tbibatheory": "The Big Bang Theory",

    # The Middle
    "tmidd": "The Middle",
    "tmid": "The Middle",

    # The Walking Dead
    "twalkdead": "The Walking Dead",
    "twalkingdead": "The Walking Dead",

    # True Detective
    "tdetective": "True detective",
    "trdetective": "True detective",
}
