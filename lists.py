"""
Lists

In Python, lists are like vector or matrix operations and are dynamics.

In C or Java: arrays
    - fixe size
In Python: Dynamics
    - Do not have a fixe size -> Create the list and add elements.
    - Any type of data

"Lists are mutable."
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

"""
List to tuple
"""

list_tuple = [1, 2, 3, 4, 5, 6, 7]
print(list_tuple)
print(type(list_tuple))

tuple_var = tuple(list_tuple)
print(tuple_var)
print(type(tuple_var))  # convert to tuple

"""
unbox of lists
"""

list_unbox = [1, 2, 3]
num1, num2, num3 = list_unbox

print(num1)
print(num2)
print(num3)
# If the number of elements presents in the lists are more than the number of the elements prints
# cause ValueError.

""""
Copy from lists - Shallow copy and Deep copy
"""
list_DeepCopy = [1, 2, 3, 4, 5]
print(list_DeepCopy)

list_DeepCopy_new = list_DeepCopy.copy()

list_DeepCopy_new.append(4)

print(list_DeepCopy)
print(list_DeepCopy_new)
# When use the list_DeepCopy.copy() is create an new list but both lists are independent.
# DEEP COPY

list_ShallowCopy = [1, 2, 3, 4, 5]
print(list_ShallowCopy)

list_ShallowCopy_new = list_ShallowCopy

list_ShallowCopy_new.append(6)

print(list_ShallowCopy)
print(list_ShallowCopy_new)
# Both lists receive the new element (6) "Not independent"
# SHALLOW COPY
