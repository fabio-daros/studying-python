"""
Positional only arguments.
"""

# Example_1: ----------------------------------------------------------------

value = '67.3'
print(float(value))


# Example_2: ----------------------------------------------------------------

def greeting_v1(name):
    return f'Hello {name}'


print(greeting_v1('[NAME]'))
print(greeting_v1(name='[NAME]'))


def greeting_v2(name, /):  # This is the argument.
    return f'Hello {name}'


print(greeting_v2('[NAME]'))
print(greeting_v2(name='[NAME]'))
