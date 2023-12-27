"""
Functions with default parameters
1 - Where the parameter is optional
"""


# Example

def square(nums):
    return nums ** 2


print(square(3))  # If dont put an value -> TypeError


# Example 2

def exponential(num, pot=2):
    return num ** pot


print(exponential(2, 3))  # 2 * 2 * 2 = 8
print(exponential(3, 2))  # 3 * 3 = 9

print(exponential(3))  # Default: Square because pot=2 for default
print(exponential(3, 5))
