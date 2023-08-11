#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
num = abs(num)
if number < 0:
    print("The last digit of", number, "is", -num, "and it is less than 6 and not 0")
elif num > 5:
    print("The last digit of", number, "is", num, "and it is greater than 5")
elif num == 0:
    print("The last digit of", number, "is", num, "and it is 0")
