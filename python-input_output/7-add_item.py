#!/usr/bin/python3
"""Add all arguments to a Python list and save to a file."""

import json

from sys import argv
from os import path

filename = "add_item.json"

if path.exists(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        my_list = json.load(file)
else:
    my_list = []

my_list.extend(argv[1:])
with open(filename, mode="w", encoding="utf-8") as file:
    json.dump(my_list, file)
