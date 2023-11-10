#!/usr/bin/python3
"""Summary."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate method."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            Return: the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Print to stdout the rectangle using '#'."""
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end='')
            print('#', end='')
            for j in range(self.__width - 1):
                print('#', end='')
            print()

    def __str__(self):
        """Return information about the rectangle."""
        name = "[Rectangle] "
        rectangle_id = "({}) ".format(self.id)
        x_and_y = "{}/{} - ".format(self.__x, self.__y)
        width_and_height = "{}/{}".format(self.__width, self.__height)
        return name + rectangle_id + x_and_y + width_and_height

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        attr = ["id", "width", "height", 'x', 'y']
        for i in range(len(args)):
            setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return information about rectangle as dictionary."""
        keys = ['id', 'width', 'height', 'x', 'y']
        rectangle_dict = {}

        for key in keys:
            rectangle_dict[key] = getattr(self, key)

        return rectangle_dict
