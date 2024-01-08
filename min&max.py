""""
Min & Max Functions

max() - returns the maximum value from an iterable or the maximum value between elements.
min() - returns the minimum value from an iterable or the minimum value between elements.
"""

# Example(s) 1 max() ---------------------------------

list_max = [1, 66, 50, 4, 40, 34, 90, 78, 9]
print(max(list_max))

tuple_max = (1, 66, 50, 4, 40, 34, 90, 78, 9)
print(max(tuple_max))

set_max = {1, 66, 50, 4, 40, 34, 90, 78, 9}
print(max(set_max))

dic_max = {'a': 1, 'b': 66, 'c': 50, 'd': 4, 'e': 40, 'f': 34, 'g': 90, 'h': 78, 'i': 9}
print(max(dic_max.values()))  # necessary the .values, else the python shows the key only.

# Example(s) 2 min() ---------------------------------

print(min(list_max))

print(min(tuple_max))

print(min(set_max))

print(min(dic_max.values()))  # necessary the .values, because the python shows the key only.

# Practice 1 example with max() ---------------------------------
# Do an code to receive two values from the users and show the major value. ---------------------------------

while True:
    try:
        val_1 = int(input('Enter the first number: '))
        val_2 = int(input('Enter the second number: '))
        break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

print(f'The greatest value informed is: {max(val_1, val_2)}')

# Practice 2 example with min() ---------------------------------
# Do an code to receive two values from the users and show the lower value. ---------------------------------
# Using the same code above ...

print(f'The lower value informed is: {min(val_1, val_2)}')

# Another examples ---------------------------------

names = ['John', 'Smith', 'Dora', 'John']

print(max(names))  # The max value test by alphabetical order.

print(min(names))  # The min value test by alphabetical order.

# Using lambda ...

print(max(names, key=lambda name: len(name)))  # The key is a function ...

print(min(names, key=lambda name: len(name)))  # The key is a function ...

# Example 3 ----------------------------------------------------------------------------------------------------

musics = [
    {'title': 'Thunderstruck', 'number_of_play': 3},
    {'title': 'Through the Valley', 'number_of_play': 6},
    {'title': 'Big Me', 'number_of_play': 2},
    {'title': 'Yellow', 'number_of_play': 9}
]

print(max(musics, key=lambda music: music['number_of_play']))

print(min(musics, key=lambda music: music['number_of_play']))

# CHALLENGE!_1 - Print only the title of the music max and min --------------------------------------

print(max(musics, key=lambda music: music['number_of_play'])['title'])  # inform the key is the answer.

print(min(musics, key=lambda music: music['number_of_play'])['title'])  # inform the key is the answer.

# CHALLENGE!_2 - Print only the title of the music without a max(), min() and lambda functions.

max = 0

for music in musics:
    if music['number_of_play'] > max:
        max = music['number_of_play']
for music in musics:
    if music['number_of_play'] == max:
        print(f'{music["title"]}')

min = 99999

for music in musics:
    if music['number_of_play'] < min:
        min = music['number_of_play']
for music in musics:
    if music['number_of_play'] == min:
        print(f'{music["title"]}')
