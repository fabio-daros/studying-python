"""
OOP - MRO - Method Resolution Order.



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
        self._Animal__name = None

    def swim(self):
        return f'{self._Animal__name} is swimming.'

    def presentation(self):
        return f'I am {self._Animal__name} from sea.'


class Land(Animal):

    def __init__(self, name):
        super().__init__(name)
        self._Animal__name = None

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
