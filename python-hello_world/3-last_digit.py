import random
number = random.randint(-10000, 10000)
number = str(number)
if(int(number[len(number) - 1]) > 5):
    print("The last digit of", int(number), "is", int(number[len(number) - 1]), "and is greater than 5")
if(int(number[len(number) - 1]) == 0):
    print("The last digit of", int(number), "is", int(number[len(number) - 1]), "and is equal to 0")
else:
# if(int(number[len(number) - 1]) < 6 and not 0  ):
    print("The last digit of", int(number), "is", int(number[len(number) - 1]), "and is less than 6 and not 0")
    



# print("The last digit of", number, "is", number[len(number) - 1])


# num = 124566788889
# num = str(num)

# print(num[len(num) - 1])
