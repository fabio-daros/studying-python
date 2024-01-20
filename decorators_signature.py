"""
Decorators with different signature

Type_1: The signature of a function is characterized by its return type, name, and parameters.
Type_2: We can use named parameters or keyword arguments.
"""
# Remembering
"""
def scream(function):
    def increase(name):
        return function(name).upper()

    return increase


@scream
def greetings(name):
    return f'Hello, my name is {name}'


@scream
def order(principal, accompaniment):
    return f'Hello!, I need {principal}, and to accompaniment {accompaniment}, please!'


# Test_1
# print(greetings('John Marston'))

print(order('Beef', 'Fries')) 

# Here we have an Error.

# To address the TypeError: 'scream.<locals>.increase()' takes 1 positional argument but 2 were given, a decorator 
pattern should be used."""


# Refactoring with a Decorator Pattern (*args, **kwargs)
# Correct form.

def scream(function):  # This is a signature from one function.
    def increase(*args, **kwargs):
        return function(*args, **kwargs).upper()

    return increase


@scream
def greetings(name):
    return f'Hello, my name is {name}'


@scream
def order(principal, accompaniment):
    return f'Hello!, I need {principal}, and to accompaniment {accompaniment}, please!'


# Testing:

print(greetings('John Marston'))

print(order('Beef', 'Fries'))

# Type_2: We can use named parameters or keyword arguments.
# Example:

print(order(accompaniment='Fries', principal='Beef'))


# Decorators with arguments (Three functions inside).

def verify_first_argument(value):
    def internal(function):
        def another(*args, **kwargs):
            if args and args[0] != value:
                return f'Incorrect value! First argument need be {value}'
            return function(*args, **kwargs)

        return another

    return internal


@verify_first_argument('pizza')
def favorite_food(*args):
    print(args)


@verify_first_argument(10)
def sum_ten(num_1, num_2):
    return num_1 + num_2


print((sum_ten(10, 12)))  # 22

print((sum_ten(1, 12)))  # Show the incorrect value to argument.

print(favorite_food('pizza', 'nachos'))

print(favorite_food('Beef', 'hot-dog'))  # Show the incorrect value to argument.
