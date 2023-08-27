#!/usr/bin/python3
"""Module for the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialize class Square
        Args:
           size: side's size of the square
           x: x-axis
           y: y-axis
        Return:
           Nothing
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Gets the size of Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the new value of Square
        Args:
           value: Size
        Return:
           Nothing
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        Return:
           Nothing
        """
        dict_order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns the dictionary
           representation of class Square.
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
