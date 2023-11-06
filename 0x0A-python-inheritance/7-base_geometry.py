#!/usr/bin/python3
"""Summary."""


class BaseGeometry:
    """A class."""

    def area(self):
        """Basegeometry's area.

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate arguments.

        Args:
            name : str
            value : int

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
