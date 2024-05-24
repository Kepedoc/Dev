x = str(input("input the filepath:"))

file = open(x,'r')
wynik = open('withoutSpaces.txt', 'w')

tab = []
tab2 = []

with open(x, 'r') as fp:
    lines = len(fp.readlines())

for x in range(lines):
    wiersz = file.readline()

for x in wiersz:
    tab.append(x)

for i in tab:
     if i == " ":
          continue
     else:
          tab2.append(i)

result = "".join(tab2)

wynik.write(result)
print("spaces have been deleted\n")
