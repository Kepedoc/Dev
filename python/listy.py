list = []
while True:
    opcja = int(input("wybiez od 1-4\n1. Dodaj imie\n2. Wypisz\n3. Usun\n4. Sortowanie\n"))
    if opcja == 1:
        imie = input("Podaj imie\n")
        list.append(imie)
        print(list)
    elif opcja == 2:
        print(list)
    elif opcja == 3:
        print(list)
        usun = input("podaj co chesz usunonc\n")
        list.remove(usun)
    elif opcja == 4:
        list.sort()
        print(list)
