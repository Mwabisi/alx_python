"""
This module contains a function that checks if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Function to check if an object is exactly an instance of a specified class.

    Parameters:
    obj: The object to check
    a_class: The class to check against

    Returns:
    True if the object is exactly an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class