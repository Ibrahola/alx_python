class Square:
    __size = None

    def __init__(self, size):
        self.size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)