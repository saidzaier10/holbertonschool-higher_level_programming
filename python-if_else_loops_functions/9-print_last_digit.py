#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints and returns the last digit of a number.
    """
    # The last digit of a positive or negative number
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
