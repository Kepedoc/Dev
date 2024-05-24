length = int(input("input how many numbers you want to add"))
tab = []
for x in range(length):
    number = int(input())
    tab.append(number)
sort = int(input("sort ascending = 1\n sort descending = 0\n"))
if sort == 1:
    tab.sort()
else:
    tab.sort()
    tab.reverse()
print(tab)
