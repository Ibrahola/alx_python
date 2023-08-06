
def raise_exception():
        name = input("Name is: ")
        print("Hello", name)


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")





# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be zero")