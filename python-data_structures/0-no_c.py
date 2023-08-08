def no_c(my_string):
    dup = ""
    for ch in my_string:
        if ch == "c":
            dup = my_string.replace("c","")
            return dup
        if ch == "C":
            dup = my_string.replace("C", "")
            return dup

print(no_c("Holberton School"))
print(no_c("Chigaco"))
print(no_c("C is fun"))

