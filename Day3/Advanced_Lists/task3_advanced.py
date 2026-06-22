numbers=[10,25,10,45,30,25,60,45,80,90,60]
unique_numbers=[]
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("original list:",numbers)
print("without duplicates:",unique_numbers)
