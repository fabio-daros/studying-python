"""
Lists

In Python, lists are like vector or matrix operations and are dynamics.

In C or Java: arrays
    - fixe size
In Python: Dynamics
    - Do not have fixe size. create the list and add elements.
    - Any type of data
"""

list_numbers = [12, 23, 344, 43, 56, 5, 7, 5]

list_letters = ['a', 'b', 'c', 'd', 'e']

list_empty = []

list_range = list(range(11))

list_string = 'hello world'

num = input('Insert a number')
if list_range[8]:
    print(f'{num} found')
else:
    print(f'No {num} found')

list_numbers.sort()
print(list_numbers)

print(list_numbers.count(5))

print(list_numbers)
list_numbers.append(42)  # Only one element
print(list_numbers)

list_numbers.append([8, 3, 1])  # List inside list
print(list_numbers)

if [8, 3, 1] in list_numbers:
    print(f'Found {list_numbers}')
else:
    print(f'{list_numbers}Not found')

list_numbers.extend([123, 55, 88])  # new elements inside my list
print(list_numbers)

list_numbers.insert(2, 99)

list_new = list_numbers + list_range  # Sum lists

list_new.reverse()  # Invert the list

print(list_numbers)
print(list_letters)
print(list_empty)
print(list_range)
print(list_string)
print(list_new)
print(len(list_new))

course = 'new,course,from,udemy'
print(course)
course = course.split(' , ')
print(course)

course = ' '.join(course)
print(course)

print(list_new)
list_new.clear()
print(list_new)

cart = []
product = ''

while product != 'exit':
    print('Add one product or insert exit to exit')
    product = input()
    if product != 'exit':
        cart.append(product)
for product in cart:
    print(product)
