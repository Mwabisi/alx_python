def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class ; otherwise False."""
    if isinstance(obj, a_class):
        return f"{obj} is an instance of the class {a_class.__name__}"
    else:
        return f"{obj} is not an instance of the class {a_class.__name__}"


print(is_same_class(5, int))  
print(is_same_class("hello", str))  
print(is_same_class(5, str))  
print(is_same_class([1, 2, 3], list))  
print(is_same_class({"a": 1}, dict))