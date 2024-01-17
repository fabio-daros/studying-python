"""
Custom modules

Python modules are archives Python, so every archive created in this study is modules.
"""
# Example 1 - Import a specific function form a module -----------------------

from functions_with_parameter import sum_odd

print(sum_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Example 2 - Import all function form a module -----------------------

import functions_with_parameter as fwp

# Access and print a variable from module.
print(fwp.list1)

print(fwp.sum_odd(fwp.list1))

# Example 3  -----------------------

from map import cities, c_for_f

print(list(map(c_for_f, cities)))
