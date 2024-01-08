"""
Integrated functions: any() and all()

1. all() -> returns True if all iterables are true or if the iterable is null.

2. any() -> returns True if any element is true.

"""

# Example 1 all() ------------------
# All numbers are true? False because have an '0'

print(all([0, 1, 2, 3, 4]))

print(all([1, 2, 3, 4]))  # True

print(all([]))  # True

print(all(['Hello World']))  # True
# ------------------
names = ['John', 'Smith', 'Camila', 'Carla', 'David', 'Mary']

print(all([name[0] == 'C' for name in names]))  # False, because we name with another word at the first character or
# position [0]
print(all([letter for letter in 'eio' if letter in 'aeiou']))  # True, because have this character on the 'eio'

# Example 1 any() ------------------

print(any([0, 1, 2, 3, 4]))  # True because one element is true.

print(any([0, False, {}, (), []]))  # False

names2 = ['Peter', 'Mark', 'Calvin', 'Cristian']

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))  # True
