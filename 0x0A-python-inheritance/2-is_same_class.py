#!/usr/bin/python3
"""Summary."""


def is_same_class(obj, a_class):
    """Check type if it matches a_class.

    Args:
        obj: an element
        a_class : type

    Returns:
        True: if obj type matches a_class
        Flase: if obj type didnt matches a_class
    """
    if type(obj) is a_class:
        return True
    return False
