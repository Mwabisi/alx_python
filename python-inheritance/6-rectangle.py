#!/usr/bin/python3
"""Module for class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle extends from  BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height