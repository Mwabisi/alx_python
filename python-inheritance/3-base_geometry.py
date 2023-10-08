class BaseGeometry:
    """
    This is a base class for geometry-related operations.
    """

    def __init__(self):
        """
        Initialize a BaseGeometry object.
        """
        pass

base_geometry = BaseGeometry()

print(f'<3-3-base_geometry.BaseGeometry object at 0x{id(base_geometry):x}>')
print(dir(base_geometry))
print(dir(BaseGeometry))