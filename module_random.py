"""
Random Module

Type_1: In Python, module is another one archive Python.

Random Modules have many functions to generate of aleatory numbers.
"""

# Example 1 - Form 1 ------------------------------------------------------------

import random

# Realize the import above; All functions, attributes, class or property is upload to memory, readies to use
# (No recommended).

print(random.random())

# random() -> A function to generate an aleatory number beside 0 and 1

"""
Type_2: Don't confuse the function random() with the package random.
"""

# Example 2 - Form 2 ------------------------------------------------------------

# import a specific function form package random:

# (Recommended).

from random import random

for i in range(10):
    print(random())
    print(i)

# Example 3 ------------------------------------------------------------
print('\n')

from random import uniform

for j in range(10):
    print(uniform(3, 7))  # Random real values between 3 and 6.

print('\n')

# Example 4 - Generate the number of integers to play the lottery --------------------------------------

from random import randint

for n in range(6):  # Six numbers to play.
    print(randint(1, 61), end=', ')  # Random real values between 1 and 60.

print('\n')

# Example 5 - choice() function -> show an aleatory value beside a iterable --------------------------------------

from random import choice

plays = ['rock', 'paper', 'scissor']

print(choice(plays))  # With choice, the Python get one and print.

print('\n')

# Example 6 - shuffle() function -> shuffle datas --------------------------------------

from random import shuffle

cards = ['k', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(cards)

shuffle(cards)

print('\n')

print(cards.pop())
