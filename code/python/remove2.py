filename = input("Enter the name of the file: ")

with open(filename, 'r') as file:
    lines = file.readlines()

with open(filename, 'w') as file:
    for i, line in enumerate(lines):
        if i % 2 == 0:
            file.write(line)