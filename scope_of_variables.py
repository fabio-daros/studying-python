"""
Scope of Variables

Two cases:

1 - Global variables
    - The recognition in all parts of the system

2 - Local variables
    - Only in the block where the variable has been declared.


In Python, it is not necessary to declare the type of variable, only the variable.

"""

number = 40  # example of global variable.
print(type(number))

name = 'John Marston'
print(type(name))

number2 = 42

if number2 > 10:
    new = number2 + 10  # Variable new is a local (if) variable.
    print(number2)

print(new)
