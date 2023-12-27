"""
List Comprehension

1. We can add conditional structures.

"""

# Example 1 ------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

pairs = [numbers for numbers in numbers if numbers % 2 == 0]
odds = [numbers for numbers in numbers if numbers % 2 != 0]

print(pairs)
print(odds)

# Refactor

pairs2 = [numbers for numbers in numbers if not numbers % 2]
odds2 = [numbers for numbers in numbers if numbers % 2]

print(pairs2)
print(odds2)

# Example 2 ------------------------------------------------

res = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]
print(res)
