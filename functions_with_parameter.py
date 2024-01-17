"""

Functions with input parameters

- Process only inside the function.

Input -> process -> output

Functions:
1 - Do not have input
2 - Do not have output
3 - Have input but do not have output
4 - Do not have input but have output
5 - Have input and output

import time


# Example:

def square(number):
    # return number * number
    return number ** 2


print(square(7))
print(square(2))
print(square(5))

ret = square(6)
print(ret)


# Refactoring the function sing_happy_birthday()

def sing_happy_birthday(birthday_person):
    print("Happy birthday to you!")
    print("Have a nice day!")
    print(f"To you!, to you! {birthday_person}")


sing_happy_birthday("NAME")

print('\n')


# Example 2
def sing_happy_birthday(name):
    lyrics = [
        "Happy Birthday to you!",
        "Happy Birthday to you!",
        "Happy Birthday dear " + name + "!",
        "Happy Birthday to you!",
    ]

    for line in lyrics:
        print(line)
        time.sleep(1)  # Add a pause for dramatic effect


# Example usage:
sing_happy_birthday("NAME")


# function with many parameters

def concat(a, b):
    return a + b


def multiply(num1, num2):
    return num1 * num2


def other(num1, b, msg):
    return (num1 + b) * msg


print(concat(2, 5))
print(concat(10, 20))
print(multiply(4, 5))
print(other(2, 3, "Hello"))


# Named parameters

def complete_name(first_name, last_name):
    return first_name + " " + last_name


# Parameters are vars declared in the definition of the function.
# Arguments are data pass during the execution of a function.
# The order of parameters is important.

print(complete_name("FIRST_NAME", "LAST_NAME"))

# Named arguments or (Keywords arguments)

print(complete_name(first_name="FIRST_NAME", last_name="LAST_NAME"))


# Common error in returns
"""


def sum_odd(nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total = total + num
        return total  # this return is in a wrong place


"""To use in the dunder.py module"""

if __name__ == '__main__':
    list_1 = [1, 2, 3, 4, 5, 6, 7]
    print(sum_odd(list_1))

    tuple = (1, 2, 3, 4, 5, 6, 7)
    print(sum_odd(tuple))
