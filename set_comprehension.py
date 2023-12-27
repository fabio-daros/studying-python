"""
Set Comprehension

List = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""

# Example 1 --------------------------------

nums = {num for num in range(1, 7)}
print(nums)

# Example 2 --------------------------------

nums2 = {x ** 2 for x in range(10)}
print(nums2)

# Challenge: Modify the last structure to generate a dict --------------------------------

nums3 = {x: x ** 2 for x in range(10)}  # To complete the challenge, use the x like key -> (x:)...
print(nums3)

# To finish --------------------------------

letters = {letter for letter in 'Hello World!'}  # without ordered and repetition
print(letters)
