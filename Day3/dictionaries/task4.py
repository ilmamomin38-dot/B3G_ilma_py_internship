words=["apple","ant","banana","bat","cat","carrot"]

grouped={}

for wor in words:
    letter=words[0]
    grouped.setdefault(letter,[]).append(words)
print(grouped)
