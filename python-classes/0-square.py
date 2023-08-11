#!/user/bin/phython3
class Square:
    def __init__(self, size):
        self.__size = size

        square = Square(4)
        print(Square.__dict__)
        print(square._Square__size) # type: ignore