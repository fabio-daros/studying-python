"""
Documentation for docstrings

PS1: We can access the documentation as the python function, utilizing the special method __doc__

PS2: We can access the documentation with the function help()
"""


#  Example 1

def say_hello():
    """A simple function to return a hello."""
    return "Hello!"


#  Example 2

def exponential(number, potential=2):
    """
    A simple exponential function
    :param number:
    :param potential:
    :return:
    """
    return number ** potential
