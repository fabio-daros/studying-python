"""
PDB -> Python Debugger

Bug ->

"""

# Example 1 ------------------------
# The utilization of the print to debug, is a badly form to debug.

"""
def division(a, b):
    print(f'Values to division: a = {a} and b = {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'An Problem occurred: {err}'


print(division(4, 7))
"""


# Example 3 PDB with PyCharm ------------------------
# In Python, can be used different IDEs like PyCharm or utilize the PDB.

def division(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'An Problem occurred: {err}'


print(division(4, 7))
