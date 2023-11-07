#!/usr/bin/python3
"""Summary."""
import json


def save_to_json_file(my_obj, filename):
    """Save json data into a file.

    Args:
        my_obj (dict): json data.
        filename (str): file name data will be writen into.
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, indent=4))
