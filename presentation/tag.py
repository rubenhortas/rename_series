from .color import Color


# noinspection PyClassHasNoInit
class Tag:
    """
    Defines the tags for each message shown in the output.
    """

    error = "[" + Color.bold_red + "ERROR" + Color.end + "]"
    info = "[" + Color.green + "*" + Color.end + "]"
    warning = "[" + Color.bold_yellow + "WARNING" + Color.end + "]"
    move = Color.bold_yellow + "->" + Color.end
    debug = ">>"
    ex = "[" + Color.bold_red + "EXCEPTION!" + Color.end + "]:"
