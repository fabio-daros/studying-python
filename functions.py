"""
Functions:

- Functions are minor extensions of the code to realize specific works.
- Receive an input and return an output of data.
Example:
    - print()
    - len()
    - max()
    - min()
    - count()
    - etc...
"""
"""
# Example of function:

colors = ['red', 'green', 'blue', 'white']
print(colors)

course = 'Python for dumbs'
print(course)

colors.append('purple')  # Add an element to the list (final)
print(colors)

# course.append('More items') # AttributeError
# print(course)

colors.clear()  # Clear the list
print(colors)

print(help(print))
# DRY - Don't repeat yourself


How define functions in Python?:
Example:

def name_function(input_parameter)
    function...
    
PS: "def" is an reserved word of the python to define a function.
"""


# My first function:

def say_hello():
    print("Hello!")


"""
PS:
1 - Inside the function its possible use another function.
2 - This function do only one thing - say hello!
3 - This function do not receive any argument.
4 - This function do not return anything.
"""
# Use the function to say hello:
say_hello()


# Example 2

def sing_happy_birthday():
    print("Happy birthday to you!")
    print("Have a nice day!")
    print("To you!, to you!")


for n in range(3):
    sing_happy_birthday()

sing = sing_happy_birthday
print(sing)
