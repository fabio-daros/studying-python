"""
Reduce

PS: Python3 and other new versions, reduce() not be more integrated version (built-in) now we need import.

To understand reduce()

# In one collection of datas:

Datas = [a1, a2, a3, a4 ... an]

# And you have a function that receiving two parameters

Def function(x, y)
    return x * y

The function 'reduces()', for example

    Pass 1: res1 = f(a1, a2) # Apply the function in the two first elements and accumulate the result.
    Pass 2: res2 = f(res1, a3) # Apply the result of function res1 and the third element and accumulate the res
        This repeat to the end
        Pass 3: res3 = f(res2, a4)


We can see the reduce function like:
function (function (function (a1, a2), a3), a4) ...), an)
"""

# Example 1  --------------------------
# Multiply all numbers from a list

from functools import reduce

datas = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# To use the reduce() We can use one function to receive two parameters.

multi = lambda x, y: x * y

res = reduce(multi, datas)
print(res)

# The same, but using a normal loop: --------------------------

res2 = 1

for n in datas:
    res2 = res2 * n

print(res2)

# PS -> Loop for is more legible to create a function without reduce()
