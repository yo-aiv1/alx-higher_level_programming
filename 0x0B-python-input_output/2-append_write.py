#!/usr/bin/python3
"""Summary."""


def append_write(filename="", text=""):
    """Append text in a file.

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): text that will be writen. Defaults to "".

    Returns:
        int: number of chars
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return (len(text))
