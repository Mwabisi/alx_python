#!/user/bin/phython3
class Square:
    def __init__(self, size):
        self._size = size

    def size(self):
        return self._size * self._size

square = Square(3)
print(type(square))
print(square.__dict__)