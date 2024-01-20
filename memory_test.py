"""
Memory test with Generators.

Fibonacci sequence:
1, 1, 2, 3, 5, 8, 13 ...

"""


# Example_1 - With the fibonacci sequence, create a function generator. ---------
# Using lists:

def fib_list(max_value):
    nums = []
    a, b = 0, 1  # Starting variable a and b with 0 and 1.
    while len(nums) < max_value:
        nums.append(b)  # the first number is 1, so the value of 'a' is the same os 'b' or 1, append(b)...
        a, b = b, a + b
    return nums


# Testing....

for n in fib_list(100000):
    print(n)


# Example_2 - With the fibonacci sequence, create a function generator. ---------
# Using Generators:

def fib_gen(max_value):
    a, b, counter = 0, 1, 0
    while counter < max_value:
        a, b = b, a + b
        yield a
        counter = counter + 1


# Testing....

for n in fib_gen(100):
    print(n)
