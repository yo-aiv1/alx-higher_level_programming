#!/usr/bin/python3
"""Summary."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate method."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return information about the rectangle."""
        name = "[Square] "
        square_id = "({}) ".format(self.id)
        x_and_y = "{}/{} - ".format(self.x, self.y)
        width_and_height = "{}/{}".format(self.width, self.height)

        return name + square_id + x_and_y + width_and_height

    @property
    def size(self):
        """Return size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value
