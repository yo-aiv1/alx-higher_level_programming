#!/usr/bin/python3
"""Summary."""
import json


def to_json_string(my_obj):
    """Turn json into a string.

    Args:
        my_obj (dict): json content

    Returns:
        str: json content as str.
    """
    return json.dumps(my_obj)
