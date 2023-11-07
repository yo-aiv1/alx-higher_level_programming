#!/usr/bin/python3
"""Summary."""


def append_after(filename="", search_string="", new_string=""):
    """Append line after the wanted string found.

    Args:
        filename (str): the file name.
        search_string (str): the wanted string.
        new_string (str): the string will be placed after the wanted.
    """
    file = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            file.append(line)
            if search_string in line:
                file.append(new_string)
        f.close()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in file:
            f.write(line)
