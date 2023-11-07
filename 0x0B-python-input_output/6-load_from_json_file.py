#!/usr/bin/python3
"""Summary."""
import json


def load_from_json_file(filename):
    """Load data from a json file.

    Args:
        filename (str): file name

    Returns:
        type of data.
    """
    with open(filename, 'r') as f:
        return json.loads(f.read())
