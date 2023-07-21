def print_comb():
    for tens_digit in range(100):
        for ones_digit in range(tens_digit + 1, 100):
            print({tens_digit:02},{ones_digit:02})

print_comb()
