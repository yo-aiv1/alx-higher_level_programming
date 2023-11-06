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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits from Basegeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle object with the given width and height.

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
