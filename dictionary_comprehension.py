""""
Dictionary Comprehension

Think…

- If We need to create a list:

List1 = [1, 2, 3, 4]

- If We need to create a Tuple:

Tuple1 = (1, 2, 3, 4)

- If We need to create a Set:

Set1 = {1, 2, 3, 4}

- If We need to create a Dictionary:

Dictionary1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Syntax:

{key:value for value in iterable}
"""

# Example 1 --------------------------------------

numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

square = {key: value ** 2 for key, value in numbers.items()}  # Every number as the dict in square.

print(square)

# Example 2 --------------------------------------

nums = [1, 2, 3, 4, 5]

square2 = {value: value ** 2 for value in nums}

print(square2)

# Example 3 --------------------------------------

keys = 'abcde'  # string
values = [1, 2, 3, 4, 5]  # list

mix = {keys[i]: values[i] for i in range(0, len(keys))}
print(mix)

# Example 4 - Conditional logic --------------------------------------

numbers = [1, 2, 3, 4, 5]

result = {num: ('pair' if num % 2 == 0 else 'odd') for num in numbers}

print(result)
