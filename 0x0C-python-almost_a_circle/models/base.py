#!/usr/bin/python3
"""Summary."""
import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate method.

        Args:
            id (int, optional): id number. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Get json representation of list_dictionaries.

        Args:
            list_dictionaries (dict)

        Returns:
            (list): representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
