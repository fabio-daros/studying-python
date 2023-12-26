"""
*Args

- The *args is a parameter. You can call anything.
1. Like *x or *y
2. But the correct is *args
3. Is used in function and create a tuple immutable.
"""


# Example 1 WITHOUT *args

def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3


print(sum_all_nums(4, 6, 9))


# But if

# print(sum_all_nums(4, 6)) # TypeError

# Example 2 WITH *args

def sum_all_nums_2(*args):
    return sum(args)


print(sum_all_nums_2())
print(sum_all_nums_2(1))
print(sum_all_nums_2(2, 3))
print(sum_all_nums_2(2, 3, 4))
print(sum_all_nums_2(3, 4, 5, 6))

print(sum_all_nums_2(23.4, 12.5))


# Example 3 WITH *args

def verify_info(*args):
    if 'Fabio' in args and 'Daros' in args:
        return 'Welcome!'
    return 'Sorry, maybe is not you!'


print(verify_info())
print(verify_info(1, True, 'Daros', 'Fabio'))  # 'Fabio' in args and 'Daros' in args -> Welcome!
print(verify_info(1, 'Daros', 3.145))  # 'Fabio' not in args and 'Daros' not in args -> 'Sorry, maybe is not you!'


# Example 4 WITH *args

def sum_all_nums_3(*args):
    return sum(args)


numbers = [1, 2, 3, 4, 5, 6, 7]  # List or Tuple is accepted less Dicts.

# UNBOXING

print(sum_all_nums_3(*numbers))  # with *var -> the argument is a collection of datas.
