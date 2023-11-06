#!/usr/bin/python3
"""Summary."""


class BaseGeometry:
    """A class."""

    def area(self, width, height):
        """Basegeometry's area.

        Raises:
            Exception: area() is not implemented
        """
        return width * height

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

    def area(self):
        """Method that returns the area of the instance."""
        return self.__width * self.__height

    def __str__(self):
        """Special method that returns the printable string."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square object with the given size.

        Args:
            size (int): square's width
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Method that returns the area of the instance."""
        return self.__size * self.__size

    def __str__(self):
        """Special method that returns the printable string."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
