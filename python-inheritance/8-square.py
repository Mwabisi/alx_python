#!/usr/bin/python3
"""
Module for class Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """Initialize an instance of the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of Square"""
        return self.__size ** 2
