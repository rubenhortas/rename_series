#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    tusubtitulocom
"""

from .get_sub_plugin import GetSubsPlugin

NAME = "tusubtitulo.com"
URL = "https://www.tusubtitulo.com"


class TuSubtituloCom(GetSubsPlugin):
    def __init__(self):
        super(TuSubtituloCom, self).__init__(NAME, URL)

    def download(self, file_name):
        super(TuSubtituloCom, self).download(file_name)
        return False
