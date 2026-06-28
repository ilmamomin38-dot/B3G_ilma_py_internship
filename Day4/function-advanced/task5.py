from functools import reduce

numbers=[12,45,7,89,34,100,56]

largest=reduce(lambda a,b,:a if a>b else b,numbers)

print("Largest number:",largest)