#!/usr/bin/python3
"""Summary."""
import json


def from_json_string(my_str):
    """Turn str to json.

    Args:
        my_str (str): json data as str

    Returns:
        dict: json data
    """
    return (json.loads(my_str))
