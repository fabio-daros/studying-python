"""
Reversed

Type: don't confuse with function reverse() from lists.

The functions reversed(), are available to any iterable.

The function reverse() returns an iterable call List Reverse Iterator

"""

# Example 1 --------------------------------------

list_1 = [1, 2, 3, 4, 5]

res = reversed(list_1)

print(res)
print(type(res))

# Can convert the element to a List, Tuple or Set.

# List
print(list(reversed(list_1)))

# Tuple
print(tuple(reversed(list_1)))

# Set
print(set(reversed(list_1)))  # Don't have an order defined.

# Can iterate in reversed
for letter in reversed('Hello World'):
    print(letter, end='')

print('\n')  # Only to present the next example in a diferent line.

# Without for
print(''.join(list(reversed('Hello World'))))  # Join transform a string in a list of strings.

# using the slice
print('Hello World'[::-1])

print('\n')  # Only to present the next example in a diferent line.

# Using the reversed() to do a loop for reverse
for n in reversed(range(0, 10)):
    print(n)

print('\n')  # Only to present the next example in a diferent line.

# Using just the range()

for n in range(9, -1, -1):
    print(n)
