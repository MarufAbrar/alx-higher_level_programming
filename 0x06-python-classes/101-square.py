#!/usr/bin/python3
"""
This module defines a Square class

Its implements value and type checks for its attributes
Attributes:
    area
    my_print
"""


class Square:
    """Square implementation
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):

        txt = ''
        if (self.__size == 0):
            pass
        else:
            for i in range(self.position[1]):
                txt += '\n'

            for i in range(self.size):
                txt += ' ' * self.position[0] + '#' * self.size

        return txt

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculates the square area
        """
        return (self.size ** 2)

    def my_print(self):
        """prints a square  with the corresponding size
        """
        print(self.__str__())

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or \
            len(position) != 2 or \
            not all(isinstance(el, int) for el in position) or \
                not all(el >= 0 for el in position):

            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position
