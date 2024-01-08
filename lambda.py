"""
Utilizing Lambda

Lambda expressions or anonymous functions.

Remembering function in Python...

def sum1(a, b)
    return a + b

"""


# Remembering function in Python ---------------------
def function(x):
    return 3 * x + 1


print(function(4))
print(function(7))

# Example 1 ---------------------
# Now the same function with lambda ---------------------

calc = lambda x: 3 * x + 1  # its necessary use a name but not like this example very poor.

print(calc(4))
print(calc(7))

# Expression with multiples values ---------------------

complete_name = lambda first_name, last_name: first_name.strip().title() + " " + last_name.strip().title()
# .strip() -> remove the spaces...
print(complete_name('Fabio', 'Daros'))

love = lambda: 'How do not love Python?'

one = lambda x: 3 * x + 1

two = lambda x, y: (x * y) ** 0.5

three = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(love())

print(one(5))

print(two(5, 7))

print(three(3, 6, 9))

# PS If we have more parameters than the arguments in lambda expression, we have a TypeError.

# Example 2 ---------------------

authors = ['Isaac Asimov', 'Ray Bradbury', 'Athur Conan Doyle', 'J.R.R Tokien', 'Frank Herbert', 'H. G. Wells',
           'Leigh Bracket', 'Orson Scot Card', 'Arthur C. Clarke']

print(authors)

# Lambda expression to order the authors with first_name and last_name ---------------------

authors.sort(key=lambda last_name: last_name.split(' ')[-1].lower())  # Order with last_name

print(authors)


# Example 3 ---------------------
# Quadratic function ---------------------
# Formula: f(x) = a * x ** 2 + b * x + c ---------------------

# Function

def generate_quadratic_function(a, b, c):
    """ Return the function: (f(x) = a*x**2+b*x+c) """
    return lambda x: a * x ** 2 + b * x + c


test = generate_quadratic_function(2, 3, -5)

print(test(0))
print(test(1))
print(test(2))
# Or
print('-------------------------')
print(generate_quadratic_function(3, 0, 1)(2))
