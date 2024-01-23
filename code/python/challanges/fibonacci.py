index = int(input("which stage?"))
num1 = 0
num2 = 1
summ = 0
i = 0
for x in range(index):
    summ = num1 + num2
    num1 = num2
    num2 = summ
    i += 1
    print(i , summ)
print(summ)
