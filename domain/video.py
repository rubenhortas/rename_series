import os
from .file import File


class Video(File):
    def __init__(self, path, file_name, testing):
        super(Video, self).__init__(path, file_name)

        if not self.is_well_formatted():
            self._remove_quality()
            self._set_episode()
            if self._is_show():
                self._set_ov()
                self._set_show_name()
                self.show_name = self._wrap_year()
                self._expand_show_name()
                self._set_episode_title()
                self._set_new_file_name()
                self._translate()
                self.new_path = os.path.join(self.path, self.new_file_name)
                self._rename_file(testing)
