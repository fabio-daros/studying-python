"""
Tuples

Tuples are used to represent lists, but we have two differences:
1 - represent with parentheses ().
2 - Tuples are immutable, when a tuple is created, this first tuple is immutable.
"""

# Caution 1: The tuples are represented with parentheses () but:

tuple_1 = (1, 2, 3, 4, 5, 6, 7)
print(tuple_1)
print(type(tuple_1))

tuple_2 = 1, 2, 3, 4, 5, 6
print(tuple_2)
print(type(tuple_2))

# Caution 2: Tuples with an unique element.

tuple_3 = 1  # This not a tuple.
print(tuple_3)
print(type(tuple_3))

tuple_4 = (2,)  # This is a tuple.
print(tuple_4)
print(type(tuple_4))
# OK, tuples has been definite to comma (,) not with parentheses.

tuple_5 = 3,
print(tuple_5)
print(type(tuple_5))  # Is tuple.

tuple_6 = tuple(range(11))
print(tuple_6)
print(type(tuple_6))  # Tuple generate with range

tuple_7 = ('Hello World', 'Python')
language, message = tuple_7

print(language)
print(message)  # PS: Error (ValueError) if a different number of element and prints.

"""
Methods to add and remove elements from a tuple do not exists, because tuples are immutable.
"""

tuple_7 = (1, 2, 3, 4, 5)
print(sum(tuple_7))
print(max(tuple_7))
print(min(tuple_7))
print(len(tuple_7))

# Concat tuples
print('Concat tuples:')
tuple_8 = (1, 2, 3)
print(tuple_8)

tuple_9 = (4, 5, 6)
print(tuple_9)

print(tuple_8 + tuple_9)  # tuples are immutable, but can be rewritten.
print('tuples are immutable, but can be rewritten.')
# Verify element
print('Verify element:')
tuple_10 = (1, 2, 3)

for n in tuple_10:
    print(n)

for index, value in enumerate(tuple_10):
    print(index, value)  # With index

# Count the number of elements in a tuple:
print('Count the number of elements in a tuple:')
tuple_11 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tuple_11.count('a'))

message = tuple('Hello World')
print(message.count('l'))

# Tuples basic are used when not necessary modify datas in a collection.
# Example:
print('Tuples basic are used when not necessary modify datas in a collection.')
print('Example:')

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
print(months)

# Access is like 'lists'
print('Access is like lists')
print(months[5])

# Iteration with while:

print('Iteration with while:')

i = 0

while i < len(months):
    print(months[i])
    i = i + 1

# Verify the month in the index:

print('Verify the month in the index:')

print(months.index('Jun'))

# Slicing
print('Slicing:')
# tuple[start:end:pass]
print(months[5:9])

print('Tuples are more fast than lists to process...')
print('Tuples made the code more efficient and secure...')

print('Copy from tuples...')

tuple_12 = (1, 2, 3)
print(tuple_12)

tuple_12_new = tuple_12

print(tuple_12_new)
print(tuple_12)

tuple_another = (4, 5, 6)

tuple_12_new = tuple_12_new + tuple_another

print(tuple_12_new)
print(tuple_12)

# In the tuple we don't have the process of Shallow Copy...
