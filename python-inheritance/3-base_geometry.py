class BaseGeometry:
    """
    This is an empty class named BaseGeometry.
    """

    def __repr__(self):
        return repr(self.__dict__)

base_geometry = BaseGeometry()

print(base_geometry)
print(base_geometry.__dict__)