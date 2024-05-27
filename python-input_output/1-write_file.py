#!/usr/bin/python3
"""Write to a file."""


def write_file(filename="", text=""):
    """Write to a file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)


# This snippet writes text to a file. The file is created if it does not exist.
