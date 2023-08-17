class Square:

    def area(self, num):
        return num * num

    def __init__(self, num):
        self.num = num


my_square = Square(3)
print("Area: {}".format(my_square.area(3)))
