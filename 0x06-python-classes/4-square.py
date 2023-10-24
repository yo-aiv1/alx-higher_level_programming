#!/usr/bin/python3
"""
Square class.

nothing
"""


class Square:
    """A class representing a square with a given size."""

    def __init__(self, size=0):
        """Initialize a new square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = int(size)

    def area(self):
        """Calculate square area.

        Returns:
            square's area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Will returns the size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Will set the size value of the square object."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
