"""
This module checks if an object is an instance of, 
or if the object is an instance of a class that was inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of a class that was inherited from, the specified class.

    Parameters:
    obj : The object to check
    a_class : The class to check against

    Returns:
    True if the object is an instance of, or if the object is an instance of a class that was inherited from, the specified class. Otherwise False.
    """
    return isinstance(obj, a_class)