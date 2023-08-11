#!/user/bin/phython3
class Square:
    def __init__(self, size):
        self.size = size

        square = Square(3)
        print(Square.__dict__)
        print(square._Square__size) # type: ignore
        print(square.size)