#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This is a class that represents a square.

    Attributes:
        None

    Methods:
        None
    """

    pass

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2
