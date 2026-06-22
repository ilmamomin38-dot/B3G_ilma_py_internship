number=[45,78,12,99,67,88,99,54]
lagest=second_largest=float('-inf')

for num in number:
    if num>lagest:
        second_largest=lagest
        lagest=num
    elif num>second_largest and num!=lagest:
        second_largest=num

        print("Second largest number:",second_largest)
        