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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save data about rectangle to a json file."""
        file_name = "{}.json".format(cls.__name__)
        list_of_dic = []

        for i in range(len(list_objs)):
            list_of_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_of_dic)

        with open(file_name, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Get json representation as string.

        Args:
            json_string (dict)

        Returns:
            (str): representation of json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)
