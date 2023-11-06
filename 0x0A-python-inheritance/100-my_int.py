#!/usr/bin/python3
"""Summary."""


class MyInt(int):
    """MyInt inherits from class int."""

    def __eq__(self, other):
        """Method that returns != check."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Method that returns == check."""
        return int.__eq__(self, other)
