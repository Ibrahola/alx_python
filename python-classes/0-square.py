#!/usr/bin/python3
Square = __import__('0-square').Square
class Square:
    def __init__(self, size):
        self.__size= size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

