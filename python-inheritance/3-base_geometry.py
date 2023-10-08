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

print(base_geometry)
print(dir(base_geometry))
print(dir(BaseGeometry))