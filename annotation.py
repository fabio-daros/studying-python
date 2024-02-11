"""
Annotations: When I write a variable with a type: "name: str"

Example:
    alignment: bool = True

"""

import math


def circumference(radius: float) -> float:
    return 2 * math.pi * radius


print(circumference.__annotations__)  # With __annotations__ I can check all about my variables.

# Example_1 of variables declarations --------------------------------

name_test: str = '[NAME]'

weight_test: float = 1.0

# Example_2 only declaration --------------------------------

active: bool

# in another part of the code:

active = True

print(active)
print(name_test)
print(weight_test)

print(__annotations__)  # With __annotations__ I can check all about variables.


# Example_3 In a class --------------------------------

class Pearson:
    def __init__(self, name: str, weight: float, age: int) -> None:  # The __init__ ever returns None...
        self.__name: str = name
        self.__weight: float = weight
        self.__age: int = age

    def walking(self) -> str:
        return f'{self.__name} is walking...'


# Instances --------------------------------

p = Pearson(name='[NAME]', weight=91.0, age=35)

print(p.__dict__)

# print(p.__annotations__) # Do not have __annotations__.

print(p.walking.__annotations__)

print(p.__init__.__annotations__)
