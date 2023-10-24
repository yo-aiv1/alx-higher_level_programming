#!/usr/bin/python3
"""
Square class.

nothing
"""

class Square:
    """A class representing a square with a given size."""
    
    def __init__(self, size = 0):
        """Initialize a new square with the given size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)