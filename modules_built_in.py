"""
Working with Built-in modules. (Integrated with Python)

Example: In the installation: /Python/Modules/BuiltIn/

"""
"""
Link to the library of all builtin modules Python:

https://docs.python.org/3/py-modindex.html
"""

# Example 1 - Using alias ----------------------------------

import random as rdm

print(rdm.random())

# Example 2 - Using '*' or (all) ----------------------------------

from random import *

print(random())

# Example 3 - Importing everything of the module ----------------------------------

import random

print(random.random())

# Example 4 - Using alias to the modules or functions ----------------------------------

from random import randint as rdi

print(rdi(5, 89))

# Example 5 - Using alias to the modules or functions with two modules ----------------------------------

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Example 6 - Multiples modules ----------------------------------
# An easy strategic is use in a tuple:

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

list_1 = ['Hello', 'World']

shuffle(list_1)

print(list_1)

print(choice('Hello'))
