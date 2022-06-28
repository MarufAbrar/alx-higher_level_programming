#!/usr/bin/python3
"""
This module implements a Square object
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialization

        Args:
            size (int): size
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """string representation

        Returns:
            str: string
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
