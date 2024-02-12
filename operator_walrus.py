"""
Operator Walrus - Python 3.8

Performs attributions and returns of values in a unique expression.

Syntax:

var := expression
"""

# Example_1  - Print a name ----------------------------------------------------------------

print(name := '[NAME]')

# Example_2  ----------------------------------------------------------------

# Old python

basket_1 = []
fruits_1 = input('Enter a fruit ')
while fruits_1 != 'exit':
    basket_1.append(fruits_1)
    fruits_1 = input('Enter a fruit ')

# Python 3.8

basket_2 = []
while (fruit_2 := input('Enter a fruit ')) != 'exit':
    basket_2.append(fruit_2)
