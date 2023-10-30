#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """A class representing a rectangle with a given size."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            widht (int): The widgh of th rectangle.
            height (int): The height of th rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Will returns the width value."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Will returns the height value."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate rectangle area.

        Returns:
            int: rectangle's area
        """
        return (self.width * self.height)

    def perimeter(self):
        """Calculate rectangle perimeter.

        Returns:
            int: rectangle's perimeter
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)
