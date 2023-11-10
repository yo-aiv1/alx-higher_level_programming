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
        square_size = "{}".format(self.size)

        return name + square_id + x_and_y + square_size

    @property
    def size(self):
        """Return size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        attr = ["id", "size", 'x', 'y']
        for i in range(len(args)):
            setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
