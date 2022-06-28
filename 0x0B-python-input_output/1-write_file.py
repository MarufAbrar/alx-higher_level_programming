#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """"write file"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
