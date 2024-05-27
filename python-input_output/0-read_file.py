#!/usr/bin/python3
"""Read a file and print its content to stdout."""


def read_file(filename=""):
    """Read a file and print its content to stdout."""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
