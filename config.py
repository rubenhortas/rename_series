#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortashortas.blogspot.com>
@contact:   rubenhortashortas at gmail.com
@github:    http://github.com/rubenhortashortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      config
"""

# ########################## Common application configuration section ########################################

# Paths containing the tv shows
SHOWS_PATHS = ["/home/rubenhortas/Vídeos", "/home/rubenhortas/Vídeos/temp"]

# ########################## rename_shows section ############################################################

# String added to the end of Original Version files
OV_STRING = "(VO)"

# Strings contained into into files downloaded from trackers in own language.
OWN_LANGUAGE_TRACKERS = ["www.DivxTotaL.com", "www.newpct1.com", "EliteTorrent.net"]

# Strings contained into into file names downloaded from trackers in original version language.
OV_TRACKERS = ["kat.cr", "[ettv]", "TASTETV", "[MPup]", "X264-DIMENSION"]

# Translations
# "Family Guy": "Padre de familia" means that if the file is named "Family Guy" the result file will be named
# "Padre de familia".
# Add your own and/or modify these.
TRANSLATED_NAMES = {
    "Family Guy": "Padre de familia",
    "Supernatural": "Sobrenatural",
    "The Simpsons": "Los Simpson",
    "Warehouse 13": "Almacén 13",
    "Warehouse13": "Almacén 13"
}

# Replace strings contained in subtitle files.
# " "(Español (España))": "VOSE" " means that if  "(Español (España))" is into the subtitle name  the result file name
#  will contains "VOSE".
# Add your own and/or modify these.
OV_SUBTITLES = {
    "(Español (España))": "VOSE",
    "(Español (Latinoamérica))": "VOSE"
}

# Video Expanded Names
# Expands abbreviated names from tv shows.
# "americanhstory": "American Horror Story" means that if the file name is "americanhstory" the result file name
# will be named "American Horror Story".
# Add your own and/or modify these.
EXPANDED_NAMES = {

    # American Dad
    "americandad": "American Dad",

    # American Horror Story
    "americanhstory": "American Horror Story",
    "ahs": "American Horror Story",
    "americanstory": "American Horror Story",
    "american horror story": "American Horror Story",

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
    "doctorwho": "Doctor Who (2005)",
    "doctorwho2005": "Doctor Who (2005)",
    "doctor who (2005)": "Doctor Who (2005)",

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
    "elmntr": "Elementary",
    "elmntry": "Elementary",
    "elementary": "Elementary",
    "elm": "Elementary",
    "elmnt": "Elementary",

    # Expediente X
    "expx" : "Expediente X",

    # Marvel's Agent Carter
    "marvelsagentcarter": "Marvel's Agent Carter",

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
    "thebigbangtheory": "The Big Bang Theory",

    # The Middle
    "tmidd": "The Middle",
    "tmid": "The Middle",
    "themiddle": "The Middle",

    # The Walking Dead
    "twalkdead": "The Walking Dead",
    "twalkingdead": "The Walking Dead",
    "twd": "The Walking Dead",

    # True Detective
    "tdetective": "True detective",
    "trdetective": "True detective",
}

# ########################## move_shows section ##############################################################

# Name of the season in the disks containing organized tv shows in format <SHOW NAME>/<SEASON>/<EPISODES>.
SEASON_PATH_NAME = "Temporada"

# Disks containing non organized tv shows
BUFFER_DISKS = ["/home/rubenhortas/Lab/fakedDestBuffer"]

# Disks containing organized tv shows in format <SHOW NAME>/<SEASON>/<EPISODES>
FINAL_DISKS = ["/media/rubenhortas/3tb"]
