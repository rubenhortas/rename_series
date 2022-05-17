from .get_sub_plugin import GetSubsPlugin

NAME = "tusubtitulo.com"
URL = "https://www.tusubtitulo.com"


class TuSubtituloCom(GetSubsPlugin):
    def __init__(self):
        super(TuSubtituloCom, self).__init__(NAME, URL)

    def download(self, file_name):
        super(TuSubtituloCom, self).download(file_name)
        return False
