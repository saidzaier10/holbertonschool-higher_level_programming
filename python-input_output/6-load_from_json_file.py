#!/usr/bin/python3
"""Load a JSON file."""


import json


def load_from_json_file(filename=""):
    """Load a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
