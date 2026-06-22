words = ["apple", "banana", "avocado", "blueberry", "cherry"]

grouped = {}
for word in words:
    first_letter = word[0]
    grouped.setdefault(first_letter, []).append(word)

print(grouped)