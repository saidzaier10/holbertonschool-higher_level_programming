#!/usr/bin/python3
"""Convert a class to a JSON string."""

import json


def class_to_json(obj):
    """Convert a class to a JSON string."""
    return obj.__dict__
