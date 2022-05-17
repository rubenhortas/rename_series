import os

from crosscutting.condition_messages import print_error
from crosscutting.constants import SUBTITLE_EXTENSIONS
from crosscutting.constants import VIDEO_EXTENSIONS
from crosscutting.messages_move_series import print_mv


def is_video(f):
    file_extension = os.path.splitext(f)[1].replace(".", "")
    if file_extension in VIDEO_EXTENSIONS:
        return True
    else:
        return False


def is_subtitle(f):
    file_extension = os.path.splitext(f)[1].replace(".", "")
    if file_extension in SUBTITLE_EXTENSIONS:
        return True
    else:
        return False


def is_python(f):
    file_extension = os.path.splitext(f)[1]
    if file_extension == ".py":
        return True
    else:
        return False


def get_videos(path):
    """
    get_videos(dest_path)
        Gets video files from a directory.
    Arguments:
        path: (string) Path.
    """

    videos = []

    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if is_video(f):
                videos.append(f)

    return sorted(videos)


def get_subtitles(path):
    """
    get_subtitles(dest_path)
        Gets subtitle files from a directory.
    Arguments:
        path: (string) Path.
    """

    subtitles = []

    files = os.listdir(path)

    for f in files:
        if os.path.isfile(os.path.join(path, f)):
            if is_subtitle(f):
                subtitles.append(f)

    return sorted(subtitles)


def mv(orig, dest, testing):
    """
    mv(orig, dest, debugging, testing)
        Moves all the files to the same directory.
    Arguments:
        orig: (string) Directory where the files will be gotten.
        dest: (string) Directory where the files will be moved.
        testing: (boolean) Indicates if the program is in testing mode.s
    """

    try:
        orig_file_name = os.path.basename(orig)
        dest_file_name = os.path.basename(dest)

        print_mv(orig_file_name, dest_file_name)

        if not testing:
            os.rename(orig, dest)
    except Exception as ex:
        print_error(ex)
