"""
**Kwargs

Can call -> **x or **y
1. The correct is **kwargs
2. Is created a tuple
3. It Is created to a Dict.

"""


# Example 1

def favorite_colors(**kwargs):
    for pearson, pearson_color in kwargs.items():
        print(f'The favorite color of {pearson} is {pearson_color}')
    print(kwargs)


favorite_colors(Joel='green', Gabi='yellow', Fabio='blue')


# Example 2 (complex)

def special_hello(**kwargs):  # Is a Dict.
    if 'Hi' in kwargs and kwargs['Hi'] == 'Hello':
        return 'You receive a special Pythonic hello'
    elif 'Hi' in kwargs:
        return f"{kwargs['Hi']} Hi"
    return 'Maybe not really you...'


print(special_hello())
print(special_hello(Hi='Python'))
print(special_hello(Hi='Hello'))
print(special_hello(Hi='special'))

"""
# IMPORTANT!
# In functions We can have:
# 1. Mandatory parameters.
# 2. Optional parameters or non default.
# 3. *args
# 4. **kwargs
"""


# Example 3

def my_func(age, name, *args, state=False, **kwargs):
    print(f'My name is {name} and i have {age} years old')
    print(args)
    if state:
        print('Lonely')
    else:
        print('Married')
    print(kwargs)


my_func(8, 'Julian')
my_func(18, 'Felicity, 4, 5, 3', state=True)
my_func(34, 'John', I='Not', you='Go')
my_func(19, 'Carl', 9, 4, 3, java=False, python=True)


# The importance of parameter order.
# Function with correct order
def show_info(a, b, *args, instructor='John', **kwargs):
    return [a, b, args, instructor, kwargs]


"""
a = 1
b = 2
args = (3,)
instructor = 'John'
kwargs = {'last_name': 'Daros', 'role': 'instructor'}
"""

print(show_info(1, 2, 3, last_name='Daros', role='instructor'))


# [1, 2, (3,), 'John', {'last_name': 'Daros', 'role': 'instructor'}]

# The importance of parameter order.
# Function with incorrect order

def show_info2(a, b, instructor='John', *args, **kwargs):
    return [a, b, args, instructor, kwargs]


print(show_info2(1, 2, 'Dean', last_name='Daros', role='instructor'))


# [1, 2, (), 3, {'last_name': 'Daros', 'role': 'instructor'}]


# Unpack with **kwargs


def show_names(**kwargs):
    return f'{kwargs["first_name"]} {kwargs["last_name"]}'


names = {'first_name': 'John', 'last_name': 'Jones'}

print(show_names(**names))  # with ** unpack the dict in names.


# Another example with unpacking.


def sum_multiples_nums(a, b, c):
    print(a + b + c)


list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
set1 = {1, 2, 3}

sum_multiples_nums(*list1)  # UNPACK
sum_multiples_nums(*tuple1)  # UNPACK
sum_multiples_nums(*set1)  # UNPACK

dict1 = dict(a=1, b=2, c=3)

sum_multiples_nums(**dict1)  # Unique form to UNPACK a Dict.

# PS: The names of the keys in a dict can be the same os the parameters of the function.
