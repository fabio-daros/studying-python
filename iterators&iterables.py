"""
Iterators and Iterables.

1. Iterator
    - An object that can be iterated.
    - An object that can return data with just one element when the function next() is called.

2. Iterable
     - An object that returns an iterator when the function iter() is called.
"""

# Example_1 ---------------------------------
# Mechanic occurred inside the Python:

name = 'Name'  # Is an iterable, but not is an iterator.
nums = [1, 2, 3, 4, 5, 6]  # Is an iterable, but not is an iterator.

it_1 = iter(name)  # Transforming
it_2 = iter(nums)  # Transforming

print(next(it_1))  # N
print(next(it_1))  # a
print(next(it_1))  # m
print(next(it_1))  # e -> The last letter.

print('\n')

print(next(it_2))  # 1
print(next(it_2))  # 2
print(next(it_2))  # 3
print(next(it_2))  # 4
print(next(it_2))  # 5
print(next(it_2))  # 6 -> The last number from the 'nums' iterable.

print('\n')

# Example_2 ---------------------------------
# How the programmer write:

for letter in name:
    print(f'{letter}')
