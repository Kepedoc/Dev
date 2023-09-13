binary = []
number = int(input("input a number:\n"))
devision = 1
while devision > 0:
    devision = number // 2
    left = number % 2
    binary.append(left)
    number = devision
print(binary)
