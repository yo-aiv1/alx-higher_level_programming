#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """A class representing a rectangle with a given size."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            widht (int): The widgh of th rectangle.
            height (int): The height of th rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return rectangle as str of "#".

        Returns:
            str: rectangle
        """
        count = 0
        _rectangle = ""
        for i in range(Rectangle.area(self)):
            if count == self.width:
                _rectangle += "\n"
                count = 0
            _rectangle += str(self.print_symbol)
            count += 1
        return _rectangle

    def __repr__(self):
        """Return the string represantion of the instance.

        Returns:
            str: object's represantion.

        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compair rectangle by area.

        Args:
            rect_1 (int): area
            rect_2 (int): area

        Returns:
            str: the bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
