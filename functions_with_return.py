"""
Functions with return


Numbers = [1, 2, 3]
ret_pop = numbers.pop()
print(f'Return of the pop: {ret_pop}')

Ret_pr = print(numbers)
print(f'Return of the print: {ret_pr}')

PS about return
1 - Finalize the function and quit the execution.
2 - Its possible to have many returns.
3 - Return anything type os data.

"""
from random import random


# Example 1

# Python functions need the reserved word return to return anything.

def square_root():
    return 7 * 7


# Using a var to receive the function return.
ret = square_root()
print(f'The return of the square_root is {ret}')


def say_hello():
    return 'Hello!'
    # print('I dont be execute because have an return statement')


print(say_hello())

people = 'Peter'
print(say_hello() + people)


# Example 2

def new_function():
    variable = False
    if variable:
        return 4
    elif variable is None:
        return 3.2
    return 'b'


print(new_function())


# Example 3

def another_function():
    return 2, 3, 4, 5


print(another_function())


# Example 4
# Function to play coin

def play_coin():
    if random() < 0.5:
        return 'Head'
    return 'Tail'


print('The play coin is: ' + play_coin())


# Common errors or unnecessary codification

def is_even():
    num = 5
    if num % 2 != 0:
        return True
    return False


print(f'The is_even function says: 5 is {is_even()}')
