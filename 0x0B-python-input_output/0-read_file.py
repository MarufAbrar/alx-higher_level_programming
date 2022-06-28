#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
