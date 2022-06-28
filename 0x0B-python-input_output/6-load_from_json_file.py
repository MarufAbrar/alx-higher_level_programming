#!/usr/bin/python3
"""load from json"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
