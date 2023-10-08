class BaseGeometry:
    """
    This is an empty class named BaseGeometry.
    """

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __sizeof__(self):
        pass

base_geometry = BaseGeometry()

print(f'<3-{base_geometry.__class__.__module__}.{base_geometry.__class__.__name__} object at {hex(id(base_geometry))}>')
print(dir(base_geometry))
print(dir(BaseGeometry))