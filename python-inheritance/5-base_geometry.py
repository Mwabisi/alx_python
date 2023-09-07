#!/usr/bin/python3
"""Module for class BaseGeometry"""

class BaseGeometry():
    """
        Class BaseGeometry
    """
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validate that value is an integer and
            greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))