#!/usr/bin/python3
"""Summary."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate method."""
        self._width = width
        self._height = height
        self._x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set width."""
        self._width = value

    @property
    def height(self):
        """Return height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set height."""
        self._height = value

    @property
    def x(self):
        """Return x."""
        return self._x

    @x.setter
    def x(self, value):
        """Set x."""
        self._x = value

    @property
    def y(self):
        """Return y."""
        return self._y

    @y.setter
    def y(self, value):
        """Set y."""
        self._y = value
