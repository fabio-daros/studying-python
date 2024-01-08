"""
Sorted

Type: Do not confound with the sort() function in Python 3 in Lists.

You Can use the sorted() function in Python to any iterable.

Type: Use to order the list.
"""

# Example 1 ----------------------------

nums = [6, 1, 8, 2]

print(nums)

print(sorted(nums))  # Order from smallest to largest number.

print(nums)

"""
Type: sorted() don't modify the original list like the sort()
"""

# Add parameters to the sorted()

print(sorted(nums, reverse=True))  # Order from largest to smallest number (reverse).

print(tuple(sorted(nums)))  # Convert to tuple.

print(nums)

print(set(sorted(nums)))  # Convert to set.

print(nums)

"""
Type: We can use the sorted() function to solve complex problems.
"""

# Example 2 ----------------------------
# tweeter users ----------------------------
users = [
    {'username': 'Daros', 'tweets': ["I love cakes", "I love pizzas"]},
    {'username': 'Jam', 'tweets': ["I love my cat"]},
    {'username': 'Livia', 'tweets': []},
    {'username': 'Dean', 'tweets': [], "color": "yellow"},
    {'username': 'Doggo_Owner', 'tweets': ["I love my dogs", "I will go away"]},
    {'username': 'Galgo', 'tweets': ["I Hate cheese!"], "color": "green"}
]

# order with the len of dict

# to use sorted() function is necessary set a key to one dict of datas.
# lambda function to username order.
print(sorted(users, key=lambda user: user['username']))

# Order to number of tweets:
print(sorted(users, reverse=True, key=lambda user: len(user['tweets'])))

# Example 3 ----------------------------

musics = [
    {'title': 'Thunderstruck', 'number_of_play': 3},
    {'title': 'Through the Valley', 'number_of_play': 6},
    {'title': 'Big Me', 'number_of_play': 2},
    {'title': 'Yellow', 'number_of_play': 9}
]
# Order with the number of plays.
print(sorted(musics, key=lambda music: music['number_of_play']))
# inverse of the list
print(sorted(musics, key=lambda music: music['number_of_play'], reverse=True))
