#!/usr/bin/python3
"""Summary."""


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
