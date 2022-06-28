#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If too long, cut the tuple to the first 2 elements
    # if too short, extend the tuple to match length 2
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    c = [x + y for x, y in zip(a, b)]
    return tuple(c[0:2])
