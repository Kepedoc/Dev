numbers = []
x = int(input("how many numbers do you want to add?\n"))
for x in range(x):
    number = input()
    numbers.append(number)
option = input("asc: sort asc\ndesc: sort desc\nEXIT\n")
match option:
    case "asc":
        numbers.sort()
        print(numbers)
    case "desc":
        numbers.sort()
        numbers.reverse()
        print(numbers)
    case "EXIT":
        exit()
