"""
OOP - Super method

The method super() is responsible to access the superclass

"""


# Example_1: Super method

class Animal:

    def __init__(self, name, specie):
        self.__name = name
        self.__specie = specie

    def vocalization(self, sound):
        print(f'The vocalization of the {self.__name} is {sound}')


class Cat(Animal):

    def __init__(self, name, specie, race):
        Animal.__init__(self, name, specie)  # Using the constructor to access the superclass. -> BAD FORMAT.
        # super().__init__(name, specie)  # Using the super() to access the superclass -> GOOD FORMAT.
        # Type_1: With super() not is necessary the use of the self like the first attribute.
        self.__race = race


felix = Cat('Felix', 'Animal', 'Persian')

felix.vocalization('Meow.')
