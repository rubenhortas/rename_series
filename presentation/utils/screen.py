#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os


def clear_screen():
    """
    clear_screen()
        Clears the screen.
    """

    if "nt" in os.name:
        os.system("cls")
    elif "posix" in os.name:
        os.system("clear")
