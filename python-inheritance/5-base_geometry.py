#!/usr/bin/python3
"""Module for class BaseGeometry"""

class BaseGeometry:
    """Defines class BaseGeometry"""

    def area(self):
        """Definition of area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if argument is an integer
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
s