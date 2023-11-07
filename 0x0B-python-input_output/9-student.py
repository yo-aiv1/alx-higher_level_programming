#!/usr/bin/python3
"""Summary."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Instantiate method.

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: dictionary representation of the class
        """
        return self.__dict__
