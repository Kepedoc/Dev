list = []
sum = 0
print("type 5 random numbers!\n")
for x in range(5):
    x = int(input())
    if x % 2 == 0:
        x = pow(x,2)
        list.append(x)
for x in list:
    sum += x
print(sum)
