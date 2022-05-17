from presentation.color import Color
from presentation.tag import Tag


def print_header(current_disk, testing):
    """
    print_header()
        Print a couple of introduction lines

    Args:
        testing:
        current_disk:
    """

    header_msg = "{0} Renaming files in {1}{2}{3}".format(Tag.info, Color.bold_red, current_disk, Color.end)

    if testing:
        header_msg = "{0} {1}[TEST]{2}".format(header_msg, Color.bold_red, Color.end)

    print(header_msg)
