"""
List Comprehension

1. Utilizing List Comprehension, We can generate new lists with processed data.

# syntax:

[Data for data in iterable]
"""
# Example 1 --------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8]

res1 = [num * 10 for num in nums]  # To each number of the list nums, multiply for 10.

print(res1)

# Example 2 --------------------------------

res2 = [num / 2 for num in nums]

print(res2)


# Example 3 --------------------------------

def func(value):
    return value * value


res3 = [func(num) for num in nums]

print(res3)

# Example 4 --------------------------------
# Using Traditional Loop --------------------------------

nums2 = [1, 2, 3, 4, 5]
double_nums = []

for number in nums2:
    double_num = number * 2
    double_nums.append(double_num)

print(double_nums)

# Using List Comprehension --------------------------------

print([number * 2 for number in nums2])  # -------------------------------- IT'S SO EASY… ONLY IN PYTHON!

# Example 5 --------------------------------

name = 'Fabio Daros'

print([letter.upper() for letter in name])  # -------------------------------- IT'S SO EASY… ONLY IN PYTHON!
