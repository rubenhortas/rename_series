import re


PATTERN_1 = re.compile("[0-9]{1,2}x[0-9]{1,2}")  # 1x20
PATTERN_2 = re.compile("[Ss][0-9]{1,2}[Ee][0-9]{1,2}")  # S1E20 or S01E20
PATTERN_3 = re.compile("\[Cap.[0-9]*\]")  # [Cap.120]
PATTERN_4 = re.compile("[0-9]{3,6}")  # 120


class Episode:

    episode_in_file_name = None
    episode_formatted = None

    def __init__(self, file_name):
        self.__get_ep_format_1(file_name)

        if self.episode_formatted is None:
            self.__get_ep_format_2(file_name)

            if self.episode_formatted is None:
                self.__get_ep_format_3(file_name)

                if self.episode_formatted is None:
                    self.__get_ep_format_4(file_name)

    def __get_ep_format_1(self, file_name):  # 1x20
        """
        __get_ep_format_1(self, file_name)
            Gets the episode if is in 1x20 format.
        Arguments:
            - file_name: (string) File name.
        """

        match = PATTERN_1.search(file_name)

        if match:
            self.episode_in_file_name = match.group(0)
            self.episode_formatted = self.episode_in_file_name

    def __get_ep_format_2(self, file_name):  # S1E20 or S01E20
        """
        __get_ep_format_2(self, file_name)
            Gets the episode if is in 1E20 or S01E20 format.
        Arguments:
            - file_name: (string) File name.
        """

        match = PATTERN_2.search(file_name)

        if match:
            episode_in_file_name = match.group(0)

            if "S0" in episode_in_file_name:
                episode = episode_in_file_name.replace("S0", "")

            elif "s0" in episode_in_file_name:
                episode = episode_in_file_name.replace("s0", "")

            elif "S" in episode_in_file_name:
                episode = episode_in_file_name.replace("S", "")

            else:  # only "s" is in file name
                episode = episode_in_file_name.replace("s", "")

            if "E" in episode_in_file_name:
                episode = episode.replace("E", "x")
            else:
                episode = episode.replace("e", "x")

            self.episode_in_file_name = episode_in_file_name
            self.episode_formatted = episode

    def __get_ep_format_3(self, file_name):  # Format [Cap.120]
        """
        __get_ep_format_3(self, file_name)
            Gets the episode if is in [Cap.120] format.
        Arguments:
            - file_name: (string) File name.
        """

        match = PATTERN_3.search(file_name)

        if match:
            episode_in_file_name = match.group(0)
            self.__get_ep_format_4(episode_in_file_name)

            self.episode_in_file_name = episode_in_file_name

    def __get_ep_format_4(self, file_name):  # Format 120
        """
        __get_ep_format_4(self, file_name)
            Gets the episode if is in 120 format.
        Arguments:
            - file_name: (string) File name.
        """

        match = PATTERN_4.search(file_name)

        if match:
            match_group = match.group(0)

            if int(match_group[:-2]) < 19:  # Skip years 19xx;20xx
                if len(match_group) % 2 == 0:
                    episode_in_file_name = match_group[-4:]
                    episode = episode_in_file_name[-2:]
                    season = episode_in_file_name[-3:-2]

                else:
                    episode_in_file_name = match_group[-3:]
                    episode = episode_in_file_name[-2:]
                    season = episode_in_file_name[-4:-2]

                self.episode_in_file_name = episode_in_file_name
                self.episode_formatted = "{0}x{1}".format(season, episode)
