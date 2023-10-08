def is_same_class(obj, a_class):
    """
    Returns a string message stating whether the object is exactly an instance of the specified class or not.

    Args:
        obj: An instance whose type we want to compare.
        a_class: The class we want to check the instance against.

    Returns:
        String message indicating whether the object is an instance of the class or not.
    """
    if type(obj) is a_class:
        return f"{obj} is an instance of the class {a_class.__name__}"
    else:
        return f"{obj} is not an instance of the class {a_class.__name__}"