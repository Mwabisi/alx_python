def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False."""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)

class ParentClass:
    pass
class ChildClass(ParentClass):
    pass

obj1 = ParentClass()
obj2 = ChildClass()

print(is_kind_of_class(obj1, ParentClass))
print(is_kind_of_class(obj2, ParentClass))
print(is_kind_of_class(obj2, ChildClass))
print(is_kind_of_class(obj1, ChildClass))
print(is_kind_of_class("hello", str))
print(is_kind_of_class(5, int))
print([1, 2, 3], list)

