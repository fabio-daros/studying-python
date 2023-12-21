"""
Collections Modules - Counter

Collections -> High-performance Container Datatypes

Counter -> Receive an iterable object and create a collection counter, like a dict with keys and values like a quantity.
"""
from collections import Counter

list1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

result_counter = Counter(list1)

print(result_counter)
print(type(result_counter))
# Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2})
# To each element of the list, the counter create a key with the number of occurrences.
print(Counter('Hello World'))
# Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
# To each word of the string, the counter create a key with the number of occurrences (include the spaces).

# Another example:

text = ('Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the '
        'Wikimedia Foundation.')
word = text.split()
result_counter_word = Counter(word)
print(result_counter_word)

# found the most 5 common words in the text:
print(result_counter_word.most_common(5))
