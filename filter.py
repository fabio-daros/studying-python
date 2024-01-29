"""
Filters

filter() -> filter the data from a collection.

"""
import statistics

# Example 1 --------------------------

values = 1, 2, 3, 4, 5, 6

avg = sum(values) / len(values)

print(avg)

# Example 2 --------------------------
# Datas from anyon sensor:

datas = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# function mean()

avg2 = statistics.mean(datas)
print(avg2)

# Example 3 --------------------------

res = filter(lambda x: x > avg2, datas)  # Two parameters
print(type(res))
print(list(res))

print(f'Again: {list(res)}')  # Like in the map() function, after the use of the datas from filter(), the datas has
# been excluded from memory.

# Example 4 --------------------------
# Filter countries empty or 'none'.

countries = ['Spain', 'France', '', 'Germany', 'Sweden', '', '', 'Brazil', 'Italy', 'Germany', '']

print(countries)

res2 = filter(None, countries)

print(list(res2))

# Another form --------------------------

res3 = filter(lambda country: country != '', countries)

print(list(res3))

# The difference between map() and filter(): The map() receive two parameters, one function and one iterable and
# return one object mapping the function to any element. The filter() receive two parameters, one function and one
# iterable and return one object filtering just the elements.

# Form 1 - More complex - List of tweets --------------------------

users = [
    {'username': 'Fabio', 'tweets': ["I love cakes", "I love pizzas"]},
    {'username': 'Samuel', 'tweets': ["I love my cat"]},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': ["I love my dogs", "I go away"]},
    {'username': 'Gal', 'tweets': []}
]

# filter the inactive users from tweeter.

print(users)

inactive = list(filter(lambda user: len(user['tweets']) == 0, users))

print(inactive)

# Form 2 - More complex - List of tweets with 'not' --------------------------

inactive2 = list(filter(lambda user: not user['tweets'], users))

print(inactive2)

# Combine filter() and map() --------------------------

names = ['Vanessa', 'Ana', 'Maryan']

# Create a list of names contains 'Your instructor is {name}', But each name can be less than 5 characters.

list1 = list(map(lambda name: f'Your instructor is {name}', filter(lambda name: len(name) < 5, names)))

print(list1)
