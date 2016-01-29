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
DIR_SEASON_NAME = "Temporada"
SHOWS_PATHS = ['/home/ruben/Vídeos', '/home/ruben/Vídeos/temp']
BUFFER_DISKS = ["/home/ruben/Lab/fakedDestBuffer"]
FINAL_DISKS = ["/media/ruben/3tb"]


# File extensions
DEFAULT_SUBTITLE_EXTENSION = ".srt"
SUBTITLE_EXTENSIONS = [".srt"]
VIDEO_EXTENSIONS = [".mp4", ".avi", ".mkv"]

# Video qualities
QUALITIES = ["720p", "1080p"]

#ES_TRACKERS = ["[www.DivxTotaL.com]", "www.newpct1.com", "(Elitetorrent.net)"]

# Original Vesion name trackers
OV_TRACKERS = ["kat.cr", "[ett]"]

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

# Video Expanded Names
EXPANDED_NAMES = {
    # American Horror Story
    "americanhstory": "American Horror Story",
    "ahs":            "American Horror Story",
    "americanstory":  "American Horror Story",

    # Arrow
    "arr": "Arrow",

    # Bates Motel
    "bmotel":        "Bates Motel",
    "bamotel":       "Bates Motel",
    "batesmotel":    "Bates Motel",

    # Boardwalk Empire
    "booardempire":      "Boardwalk Empire",
    "boardwalkempire":   "Boardwalk Empire",
    "boarempire":        "Boardwalk Empire",

    # Bob"s Burgers
    "bobs burgers":  "Bob\"s Burgers",

    # Castle
    "cas": "Castle",

    # Doctor Who
    "doctor who (2005)":    "Doctor Who (2005)",
    "doctorwho":            "Doctor Who (2005)",

    # Érase una vez
    "erasevez":      "Érase una vez (Once upon a time)",
    "erase una vez": "Érase una vez (Once upon a time)",

    # El mentalista
    "ementalista":   "El mentalista",
    "mentalista":    "El mentalista",

    # Elementary
    "ele":      "Elementary",
    "elem":     "Elementary",
    "eleme":    "Elementary",
    "elmntry":  "Elementary",

    # Marvel"s Agents of SHIELD
    "marvel\"s agents of s h i e l d":   "Marvel\"s Agents of S.H.I.E.L.D.",
    "marvels agents":                    "Marvel\"s Agents of S.H.I.E.L.D.",

    # Ray Donovan
    "rdonovan": "Ray Donovan",

    # South Park
    "sp":        "South Park",
    "spark":     "South Park",
    "southpark": "South Park",

    # The Big Bang Theory
    "tbbtheory":     "The Big Bang Theory",
    "tbibatheory":   "The Big Bang Theory",

    # The Middle
    "tmidd":        "The Middle",
    "tmid":         "The Middle",

    # The Walking Dead
    "twalkdead":     "The Walking Dead",
    "twalkingdead":  "The Walking Dead",

    # True Detective
    "tdetective":    "True detective",
    "trdetective":   "True detective",
}
