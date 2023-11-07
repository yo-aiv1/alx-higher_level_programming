#!/usr/bin/python3
"""Summary."""


def write_file(filename="", text=""):
    """Write content in a file.

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): text to write in a file. Defaults to "".

    Returns:
        number of chars written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return (len(text))
