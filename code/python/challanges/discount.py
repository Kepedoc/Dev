price = float(input("input the full price:\n"))
discount = float(input("input the amount of discount %:\n"))
x = discount / 100 
discounted = x * price
result = price - discounted
print(result , "is the price after the discount\n")
