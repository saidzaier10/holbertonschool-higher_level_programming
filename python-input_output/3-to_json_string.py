#!/usr/bin/python3
"""Convert a Python object to a JSON string."""


import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON string."""
    return json.dumps(my_obj)
