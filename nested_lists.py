"""
Nested Lists

- Normal structure of data:
    1. Arrays Unidimensional
    2. Arrays Multidimensional

- In Python We have only Lists:
    1. Numbers = [1, 'b', 3.14, True, 5]
"""
# Example 1 ---------------------------------------------------

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3 x 3

print(lists)
print(type(lists))

# To Access data ---------------------------------------------------

print(lists[0][1])  # Access number 2
print(lists[2][1])  # Access number 8

# Iterated with loops ---------------------------------------------------

for list1 in lists:
    for num in list1:
        print(num)

# List Comprehension ---------------------------------------------------

[[print(value) for value in list1] for list1 in lists]

# Another Example ---------------------------------------------------
# Board with Matrix 3 x 3 ------------------------------------------------------

board = [[num for num in range(1, 4)] for value in range(1, 4)]
print(board)

# Generate a play in the board ---------------------------------------------------

hash_game = [['X' if num % 2 == 0 else 'O' for num in range(1, 4)] for value in range(1, 4)]
print(hash_game)

# Generate initial values ---------------------------------------------------

print([['*' for i in range(1, 4)] for j in range(1, 4)])  # A board empties only with '*'
