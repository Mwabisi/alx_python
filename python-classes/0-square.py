#!/user/bin/phython3
class Square:
    def __init__(self, size):
        self.__size = size  # Private instance attribute

    def __str__(self):
        return f"<class '{self.__module__}.{type(self).__name__}'>\n{self.__dict__}\n'Square' object has no attribute 'size'\n'Square' object has no attribute '__size'"

# Example usage
square = Square(3)
print(square)
