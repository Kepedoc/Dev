aList = []
length = int(input("how long is the list?\n"))
while length > 0:
    x = input("add anything:\n")
    aList.append(x)
    length -= 1
newlist = [x for x in aList if x.isnumeric()]
print(newlist)
