"""
Assertions or checks/questions

In Python, we are using the reserved word 'assert' to realize a simple affirmation utilized in the tests.

We use the 'assert' in an expression to check if it is valid or not.
    - If the expression is True, the code returns None.
    - If the expression is False, the code returns an error with type: AssertionError.

Type_1: We can specify optional argument or an error personalizes message.

Type_2: The word 'assert' can be used to anyone function or code. (Does not need to be used exclusively in test code.)

Example:
    assert 4 == 4 -> True
    assert 4 == 5 -> False

ATTENTION:
    - If a python code executed with a parameter -O, no assertions can be validated. ALL VALIDATIONS WILL BE BROKEN…
"""


# Example_1: AssertionError ----------------------------------------------------------------

def sum_positive_nums(a, b):
    assert a > 0 and b > 0, 'Numbers must be positive.'
    return a + b


ret = sum_positive_nums(2, 4)  # 6


# Example_2: AssertionError ----------------------------------------------------------------
# ret = sum_positive_nums(-2, 4)  # AssertionError
# print(ret)

def eat_fast_food(food):
    assert food in [
        'pizza',
        'burger',
        'ice cream',
        'hamburger',
        'fries',
        'hot dog'
    ], 'Enter a valid fast food.'  # AssertionError.
    return f'I eating {food}.'  # Fast food.


food = input('Enter a food with type fast food: ')
print(eat_fast_food(food))

# Example_3: -O parameter ----------------------------------------------------------------
# ATTENTION.
# Execute in the terminal: "python -O test_assertion.py"
"""
def do_something_bad(user):
    assert user.is_admin, 'Only admin do bad things.'  # If you use -O in this python file, you can destroy the system.
    destroy_all_system()
    return 'Farewell...!'
"""
