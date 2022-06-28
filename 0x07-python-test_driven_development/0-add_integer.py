#!/usr/bin/python3
"""
This module defines `add_integer`

The function returns the sum of a and b
"""


def add_integer(a, b=98):
    """adds a and b

    Args:
        a (int): term 1
        b (int, optional): term 2. Defaults to 98.

    Raises:
        TypeError: a and b must be integer

    Returns:
        int: sum of a and b
    """

    values = []
    for x, param in [(a, 'a'), (b, 'b')]:
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(param))

    return sum(values)
