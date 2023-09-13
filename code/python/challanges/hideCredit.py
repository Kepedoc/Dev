number = input("input your Credit Card number:\n")
x = number.isnumeric()
length = len(number) - 4
if x == True:    
    while length > 0:
        print("*", end="")
        length -= 1 
    print(number[-4:])
else:
    print("this is not a number\n")
