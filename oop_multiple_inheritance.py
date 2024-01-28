"""
OOP - Multiple Inheritance

Is the possible that a class inheriting from multiples another class and the child class inherits all attributes
from another other class.

Type_1: The multiple inheritance can be created in two ways.
        1. By direct multi derivation.
        2. By direct multi derivation.

Type_2: Multi derivation = multiple inheritance.
"""


# Example_1: Direct multi derivation ----------------------------------------------------------------

class Base_1:
    pass


class Base_2:
    pass


class Base_3:
    pass


class DirectMultiDerivation(Base_1, Base_2, Base_3):
    pass


# Example_2: Indirect multi derivation ----------------------------------------------------------------

class Base_1:
    pass


class Base_2(Base_1):
    pass


class Base_3(Base_2):
    pass


class IndirectMultiDerivation(Base_3):
    # IndirectMultiDerivation() inherited 'Base_3' and indirectly 'Base_1' e 'Base_2'.
    pass


"""
Type_3: Doesn't matters how type od inheritance I use (Direct or Indirect). The class that realized the 
inheritance inherited all attributes and methods from superclass.
"""


# Real Example_3: ----------------------------------------------------------------

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


class Penguin(Aquatic, Land):  # Multiple inheritance. If I alter the sequence, the resulting is different.

    def __init__(self, name):
        super().__init__(name)


# Testing ----------------------------------------------------------------


whale = Aquatic('Wally')
print(whale.swim())
print(whale.presentation())

print('\n')

horse = Land('Silver')
print(horse.walk())
print(horse.presentation())

print('\n')

penguin = Penguin('Pingu')
print(penguin.walk())
print(penguin.swim())
print(penguin.presentation())  # This presentation is from? -> Land -> MRO - Method Resolution Order
# I am Pingu from land.

print('\n')

# To know ---------------------------------------------------------------
# Object is instance of: ------------------------------------------------

print(f'penguin is instance of Penguin? {isinstance(penguin, Penguin)}')  # True
print(f'penguin is instance of Aquatic? {isinstance(penguin, Aquatic)}')  # True
print(f'penguin is instance of Land? {isinstance(penguin, Land)}')  # True
print(f'penguin is instance of Animal? {isinstance(penguin, Animal)}')  # True
print(f'penguin is instance of object? {isinstance(penguin, object)}')
# object: If a class doesn't inherit from nobody -> True
