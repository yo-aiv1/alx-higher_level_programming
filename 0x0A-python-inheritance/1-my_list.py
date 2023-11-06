#!/usr/bin/python3
"""Summary."""


class MyList(list):
    """Inherits from list.

    Args:
        list : list.
    """

    def print_sorted(self):
        """Print list ascending."""
        print(sorted(self))
