class Square:

    def __init__(self,__size):
        self.__size = __size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)