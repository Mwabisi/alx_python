"""
This module checks if an object is an instance of a class that was inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that was inherited (directly or indirectly) from the specified class.

    Parameters:
    obj : The object to check
    a_class : The class to check against

    Returns:
    True if the object is an instance of a class that was inherited from the specified class. False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class