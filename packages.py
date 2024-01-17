"""
Packages

What is a package?

1. Modules - One archive Python

2. Packages - a DIR with a collection of modules.

Type_1: Versions < 2.x.x of Python, need it be a package with an archive call: __init__.py
Type_2: In the versions > 3.x.x mustn't necessary the utilization of this archive.
"""

# Example_1 - Using the created package geek. ---------------------------

from geek import geek_1, geek_2

from geek.university import geek_3, geek_4  # Subpackages

print(geek_1.pi)

print(geek_1.function_1(4, 6))

print(geek_2.study)

print(geek_2.function_2())

print(geek_3.function_3())

print(geek_4.function_4())

# Example_2 - Specific function from package. ---------------------------

from geek.geek_1 import function_1
from geek.university.geek_4 import function_4

print(function_1(6, 9))

print(function_4())
