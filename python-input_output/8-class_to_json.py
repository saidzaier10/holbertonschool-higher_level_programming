#!/usr/bin/python3
"""Convert a class to a JSON string."""

import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_to_json_file(obj, filename):
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(obj, file)


def class_to_json(obj):
    return obj.__dict__


def class_to_json_file(obj, filename):
    save_to_json_file(class_to_json(obj), filename)


def json_to_class(json_string):
    return json.loads(json_string)


def json_file_to_class(filename):
    return json_to_class(load_from_json_file(filename))


def json_to_class_file(json_string, filename):
    class_to_json_file(json_to_class(json_string), filename)


def json_file_to_class_file(json_filename, class_filename):
    class_to_json_file(json_file_to_class(json_filename), class_filename)
