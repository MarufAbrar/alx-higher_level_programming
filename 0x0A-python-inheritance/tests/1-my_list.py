#!/usr/bin/python3
"""
This module implements a custom list object
"""


class MyList(list):
    """Custom List
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
