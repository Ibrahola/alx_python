try:
    def safe_print_division(a, b):
        return a / b
except ZeroDivisionError:
    print("None")

a = 12
b= 2

result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))