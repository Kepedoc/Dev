x = str(input("input file:"))
with open(x, 'r') as fp:
    x = len(fp.readlines())
    print('Total lines:', x)
