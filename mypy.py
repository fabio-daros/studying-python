"""
Python type check.

To install:
pip install mypy

Annotations: When I write a variable with a type: "name: str"

Example:
    alignment: bool = True

"""

# Example_1: Using MyPy ----------------------------------------------------------------

"""
In a command line execute:

------------------------
mypy [name of module.]
- mypy mypy.py
------------------------

"""


def greetings(name: str) -> str:  # here I define the type of data -> String -> Necessary to use mypy.
    return f'Hello, my name is {name}'


print(greetings('[NAME]'))


# Example_2: ------------------------------------------------------------------------------------------------

def header(text: str, alignment: bool = True) -> str:  # Hint Type
    if alignment:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, '#')


print(header('[NAME]'))

print(header('[Alignment False]', alignment=False))

# print(header('[NAME]', alignment='True'))

"""
mypy.py:42: error: Argument "alignment" to "header" has incompatible type "str"; expected "bool"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
"""
