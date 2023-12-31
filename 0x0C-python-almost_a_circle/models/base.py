#!/usr/bin/python3
"""Summary."""
import json
import os.path


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

    @classmethod
    def create(cls, **dictionary):
        """Create an instance.

        Returns:
            str: instance with all attributes.
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        file_name = "{}.json".format(cls.__name__)

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_intance = []

        for i in range(len(list_cls)):
            list_intance.append(cls.create(**list_cls[i]))

        return list_intance