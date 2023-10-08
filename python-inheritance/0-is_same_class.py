def is_same_class(obj, a_class):
    """
    Function to check if an object belongs to a specified class.
    'obj' is the object to be checked, and 'a_class' is the class type against which to check.
    Returns a string stating whether the object is an instance of the class or not.
    """
    if type(obj) is a_class:
        return f"{obj} is an instance of the class {a_class.__name__}"
    else:
        return f"{obj} is not an instance of the class {a_class.__name__}"