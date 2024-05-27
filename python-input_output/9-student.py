#!/usr/bin/python3
"""Student class."""

import json


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of a Student instance."""
        return self.__dict__

    def to_json_string(self):
        """Return the JSON string representation of a Student instance."""
        return json.dumps(self.to_json())

    @staticmethod
    def from_json_string(json_string):
        """Return a Student instance from a JSON string."""
        return Student(**json.loads(json_string))

    def save_to_file(self):
        """Save a Student instance to a file as JSON."""
        with open("{}.json".format(self.first_name), mode="w", encoding="utf-8") as file:
            file.write(self.to_json_string())

    @staticmethod
    def load_from_file(filename):
        """Load a Student instance from a file."""
        with open(filename, mode="r", encoding="utf-8") as file:
            return Student.from_json_string(file.read())
