text = "the quick brown fox jumps over the lazy dog the fox ran"
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

from collections import Counter
print(Counter(words))
print(Counter(words).most_common(2))