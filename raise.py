"""
Raise

Check the selfErrors with raise.

Type -> not a function -> Is a reserved word like def, create own exceptions and messages.

Example:
    raise TypeError('Message')
"""


# Example 1 ------------------------------------

def to_color(text, color):
    if type(text) is not str:
        raise TypeError('Text needs to be a string!')
    if type(color) is not str:
        raise TypeError('Color needs to be a string')
    print(f'The text {text} be printed in the color {color}')


to_color('Hello', 'Green')
""" 
Traceback (most recent call last):
  File "/Users/darosfabio/PycharmProjects/guppe/raise.py", line 23, in <module>
    to_color('Hello', 4)
  File "/Users/darosfabio/PycharmProjects/guppe/raise.py", line 19, in to_color
    raise TypeError('Color needs to be a string')
TypeError: Color needs to be a string 
"""


# Example 2 - Create a tuple with pre-defined colors ------------------------------------

def to_color_2(text_2, color_2):
    colors = ('Green', 'Yellow', 'Blue', 'White')
    if type(text_2) is not str:
        raise TypeError('Text needs to be a string!')
    if type(color_2) is not str:
        raise TypeError('Color needs to be a string')
    if color_2 not in colors:
        raise ValueError(f'The color need be: {colors}')
    print(f'The text {text_2} be printed in the color {color_2}')


to_color_2('Hello World', 'Black')
"""
Traceback (most recent call last):
  File "/Users/darosfabio/PycharmProjects/guppe/raise.py", line 47, in <module>
    to_color_2('Hello World', 'Black')
  File "/Users/darosfabio/PycharmProjects/guppe/raise.py", line 43, in to_color_2
    raise ValueError(f'The color need be: {colors} ')
ValueError: The color need be: ('Green', 'Yellow', 'Blue', 'White') 
The text Hello be printed in the color Green
"""
