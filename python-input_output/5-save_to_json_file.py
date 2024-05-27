#!/usr/bin/python3
"""Save an object to a file as JSON."""


import json


def save_to_json_file(my_obj, filename=""):
    """Save an object to a file as JSON."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
