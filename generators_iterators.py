"""
Generators

- Generators are Iterators:

Type_1:
    - The opposite not is true.

Type_2:
    - Generators can be created with generator functions.
    - Generator functions using the reserved word yield.
    - Generators can be created with expression generators.

Type_3:
    - Differences between functions and generator functions:
--------------------------------------------------------------------------------
| Functions:                        | Generator Functions:                     |
--------------------------------------------------------------------------------
| Use return.                       | Use yield.                               |
--------------------------------------------------------------------------------
| Only one return.                  | Can use yield multiple times.            |
--------------------------------------------------------------------------------
| When executed, return one value.  | When executed, return a generator.       |
--------------------------------------------------------------------------------

"""


# Example_1 - Generator function: ------------------------

def count_until(value_max):
    counter = 1
    while counter <= value_max:
        yield counter  # yield is like a return...
        counter = counter + 1


# Generator function not is a Generator. This function generates a generator.

gen = count_until(10)

for num in gen:
    print(num)
