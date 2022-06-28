#!/usr/bin/python3
"""save to json"""
import json


def save_to_json_file(my_obj, filename):
    """save to json"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
