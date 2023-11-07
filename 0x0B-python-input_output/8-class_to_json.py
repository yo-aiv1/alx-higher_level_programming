#!/usr/bin/python3
"""Summary."""


def class_to_json(obj):
    """Get the dictionary description with simple data structure of an object.

    Args:
        obj (class): an instance of a Class

    Returns:
        dict: dictionary description
    """
    return obj.__dict__
