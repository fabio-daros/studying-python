"""
* HDF

* Higher Order Functions or functions with greater magnitude

1. First step to understand decorators.

- When a programming language supports HDF, it indicates that there are functions that can have another function as a
return value or functions that can take other functions as arguments.
- It is possible to create variables with functions too.
- In Python, the functions are first class citizen.
"""
from random import choice


# Example_1 ---------------------------------------------------
# Example function definition:

def sum_1(a, b):
    return a + b


def subtraction_1(a, b):
    return a - b


def multiplication_1(a, b):
    return a * b


def division_1(a, b):
    return a / b


def calculate_1(num_1, num_2, function):  # This function, I call another one function and values.
    return function(num_1, num_2)


# Testing all functions:

print(calculate_1(4, 3, sum_1))

print(calculate_1(4, 3, subtraction_1))

print(calculate_1(4, 3, multiplication_1))

print(calculate_1(4, 3, division_1))

print('\n')
# Example_2 ---------------------------------------------------

# Nested functions
"""
- Functions inside functions or nested functions.

Type_1: Know too: Inner Functions
"""


def compliments(person):
    def mood():
        return choice(('Hi There ', 'Get out of here ', 'I like you very much '))  # choice from random.

    return mood() + person


# Testing:

print(compliments('John'))

print(compliments('Mary'))

print('\n')


# Example_3 ---------------------------------------------------

# Returning functions from another function.

def make_me_laugh():
    def laugh():
        return choice(('HAHAAHAHA', 'HEHEHEHEHE', 'HEUIHEIUHEIUE'))

    return laugh()


# Testing:

laughing = make_me_laugh()

print(laughing)

print('\n')

# Example_4 ---------------------------------------------------

"""
Inner functions (Internal functions / Nested functions) can access the scope of the function more external.

Example:
---------------------
def make_me_laugh():
    def laugh():
        return choice(('HAHAAHAHA', 'HEHEHEHEHE', 'HEUIHEIUHEIUE'))
    return laugh()
---------------------

The functions laugh() can access the functions make_me_laugh()
"""


def make_me_laugh_again(person):
    def laugh_a_lot():
        laugh_2 = choice(('JAJAJAJJAJAAJA', 'CRY_HAUIHAUIHIUHAU_CRY', 'YAYAYYAYAYAYYAAYA'))
        return f'{laugh_2} {person}'

    return laugh_a_lot()


# Testing:

laughing_2 = make_me_laugh_again('Noah')

print(laughing_2)
print(laughing_2)
print(laughing_2)
print('\n')
