#!/usr/bin/python3
def lookup(obj):
    """Get available attributes and methods of an object.

    Args:
        obj : object.

    Returns:
        list: available attributes and methods.
    """

    return dir(obj)
