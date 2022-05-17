import argparse
import os
import signal

from application.move_shows import get_mounted_disks
from application.move_shows import move
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from config import BUFFER_DISKS
from config import FINAL_DISKS
from crosscutting.condition_messages import print_error
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from presentation.utils.screen import clear_screen

if __name__ == "__main__":

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreter = get_interpreter_version()

    if interpreter == REQUIRED_PYTHON_VERSION:

        buffer_disks_mounted = False
        final_disks_mounted = False

        parser = argparse.ArgumentParser(description="Move some shows.")

        parser.add_argument("-to", "--to_path", dest="path", metavar="path", help="path to move the files")

        parser.add_argument("-t", "--test", dest="test", action="store_true",
                            help="Runs a single test showing the output.")

        args = parser.parse_args()
        testing = args.test
        destination_path = args.path

        paths = []

        clear_screen()

        if destination_path:
            if os.path.isdir(destination_path):
                paths.append(destination_path)
                move(paths, testing)
            else:
                print_error("{0} is not a directory.".format(destination_path))

        else:
            buffer_disks_mounted = get_mounted_disks(BUFFER_DISKS)
            final_disks_mounted = get_mounted_disks(FINAL_DISKS)

            if buffer_disks_mounted or final_disks_mounted:
                paths = buffer_disks_mounted + final_disks_mounted
                move(paths, testing)
            else:
                print_error("No mounted disks found.")

    else:
        print_error("Requires Python {0}".format(REQUIRED_PYTHON_VERSION))
        exit(0)
