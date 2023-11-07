#!/usr/bin/python3
"""Summary."""


def read_file(filename=""):
    """Read files function.

    Args:
        filename (str): filename.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for i in f.readlines():
            print(i, end='')
