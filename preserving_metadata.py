"""
Preserving metadata with wraps

1. Metadata:
    - intrinsic data in files.
        - Example: size, format, type of image.

2. Wraps:
    - Functions, like decorators.
"""
from functools import wraps


# Example_1 ------------------------------
# With Problems:

def view_log(function):
    def login(*args, **kwargs):
        """Function login, inside another funtion"""
        print(f'Function call: {function.__name__}')  # Name of the function Sum.
        print(f'Documentation: {function.__doc__}')
        return function(*args, **kwargs)

    return login


@view_log
def sum_1(a, b):
    """Sum two numbers."""
    return a + b


# print(sum_1(10, 30))

print(sum_1.__name__)  # Problem: # The Name of the sum_1 is sum and not login.

print(sum_1.__doc__)  # Problem: # The documentation os sum_1 is: Sum two numbers and not Function login,
# inside another funtion.

print('\n')


# Example_2 ------------------------------
# Refactoring the Problem above:
# 1. Import Wraps:
# 2. Input a @wraps inside the first function.


def view_log_new(function_new):
    @wraps(function_new)  # This is the only alteration.
    def login_new(*args, **kwargs):
        """Function login, inside another funtion"""
        print(f'Function call: {function_new.__name__}')  # Name of the function Sum.
        print(f'Documentation: {function_new.__doc__}')
        return function_new(*args, **kwargs)

    return login_new


@view_log_new
def sum_new(a, b):
    """Sum two numbers."""
    return a + b


# print(sum_1(10, 30))

print(sum_new.__name__)

print(sum_new.__doc__)

print(help(sum_new))
