"""
OOP - MRO - Method Resolution Order.

MRO is the order of the execution of the methods.

1. In Python, it is possible to check the order of execution methods in three different cases:
 1.1
 Class properties __mro__;
 1.2
 Method mro();
 1.3
 Help;
"""


# Example_1: ----------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.__name = name

    def presentation(self):
        return f'I am {self.__name}'


class Aquatic(Animal):

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return f'{self._Animal__name} is swimming.'

    def presentation(self):
        return f'I am {self._Animal__name} from sea.'


class Land(Animal):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return f'{self._Animal__name} is walking.'

    def presentation(self):
        return f'I am {self._Animal__name} from land.'


class Penguin(Aquatic, Land):  # Multiple inheritance. Alter the sequence (Aquatic, Land); the resulting is different.

    def __init__(self, name):
        super().__init__(name)


# Testing ----------------------------------------------------------------


penguin = Penguin('Pingu')
print(penguin.presentation())

"""
Penguin(Aquatic, Land)
Response: I am Pingu from sea.
"""

# Check the executions with __mro__ ----------------------------------------------------------------

# In the Python console:

# from oop_mro import Penguin
# Penguin.__mro__
# (<class 'oop_mro.Penguin'>, <class 'oop_mro.Aquatic'>, <class 'oop_mro.Land'>, <class 'oop_mro.Animal'>,
# <class 'object'>) -> Observe the hierarchic
