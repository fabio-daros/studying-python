"""
Len, Abs, Sum and Round

1. len() -> return the size of the iterable.
2. abs() -> return the absolute value or real value.
3. sum() -> return the sum of all elements in the iterable.
4. round() -> return a number rounded to the nearest integer -> return an integer.

"""

# Example of len()'s ------------------------------------

print(len('Hello World'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

""" Type: When utilize the len(), the Python execute __len__() or Dunder len """

print('Hello World'.__len__())

# Example of abs()'s ------------------------------------

print(abs(-5))  # return positive

print(abs(5))

print(abs(3.14))

print(abs(-3.14))  # return positive

""" Type: Don't use abs() to string """

# Example of sum()'s ------------------------------------

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))  # Example of a tax included in a price.

print(sum([3.145, 5.678]))

""" Type: Don't use sum() to string """

# Example of round()'s ------------------------------------

print(round(10.2))  # Here go to 10

print(round(10.5))  # Here go to 10

print(round(10.6))  # Here go to 11

print(round(1.2121212121, 2))  # Here go to 1.21

print(round(1.21999999, 2))  # Here go to 1.22
