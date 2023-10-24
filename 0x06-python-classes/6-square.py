#!/usr/bin/python3
"""
Square class.

nothing
"""


class Square:
    """A class representing a square with a given size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Will returns the position value."""
        return self.__position

    @position.setter
    def position(self, value):
        """Will sets the position value of a square object."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate square area.

        Returns:
            square's area
        """
        return self.__size * self.__size

    def my_print(self):
        """Print square using #."""
        if self.__size == 0:
            print()

        for i in range(self.position[1]):
            print()
        for i in range(0, self.size):
            for k in range(self.position[0]):
                print(" ", end='')
            for j in range(self.size):
                print("#", end='')
            print()
