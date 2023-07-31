
hex = "0,1,2,3,4,5,6,7,8,9,10,a,b,c,d,e,f"
for number in range(99):
    for i in hex:
        print("{} = {} * {}".format(number, (number * i)))