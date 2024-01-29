"""
OOP - Polymorphism

"Poly" -> "Much"
"Morphism" -> "Shapes"

Polymorphism:
1. When you reimplement a method present in the Father class to child class, this is called Overriding.
2. Overriding is the best representation of polymorphism.
3. With the polymorphism implemented, we alter the behavior from a method.
"""


# Example_1: ----------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.__name = name

    def vocalization(self):  # Method from Father class.
        raise NotImplementedError('The child class needs to be implement this method')

    def eat(self):
        print(f'{self.__name} is eating...')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def vocalization(self):  # Overriding class
        print(f'The dog {self._Animal__name} is barking...')


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def vocalization(self):  # Overriding class
        print(f'The cat {self._Animal__name} is meowing...')


class Rat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def vocalization(self):  # Overriding class
        print(f'The rat {self._Animal__name} is squeaking...')


# Testing:----------------------------------------------------------------

cat = Cat('Felix')
cat.eat()
cat.vocalization()

print('\n')

dog = Dog('Horus')
dog.eat()
dog.vocalization()

print('\n')

rat = Rat('Rex')
rat.eat()
rat.vocalization()
