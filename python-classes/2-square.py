class Square:

    def area(self, num):
        self.num = num
        return num * num


    def __init__(self,num):
        self.num = num


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area(3)))

my_square_2 = Square(5)
print("Area: {}".format(my_square_1.area(5)))
