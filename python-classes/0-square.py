#!/user/bin/phython3
class Square:
    def __init__(self, size):
        self._size = size

    def size(self):
        return self._size

    def set_size(self, size):
        self._size = size


square = Square(3)
square.set_size(5)
print(square.size())