#!/usr/bin/python3
def uppercase(str):
    """
    Converts a string to uppercase and prints it.
    """
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            # Convert lowercase character to uppercase
            upper_c = chr(ord(c) - 32)
        else:
            upper_c = c
        print("{}".format(upper_c), end="")
    print()
