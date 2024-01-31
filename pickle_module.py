"""
Knowing the Pickle

Saving the data in binary format

1. Python object -> Binary.

2. Binary -> Python object.

Type_1: This process is called serialization / deserialization

Type_2: The Pickle module doesn't have any type of security. So don't be recommended to work with data non-verifiable.
"""

# Example_1: Pickle module ----------------------------------------------------------------

import pickle


class Animal:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def eat(self):
        print(f'{self.__name} is eating...')


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def vocalization(self):
        print(f'{self.name} is meowing...')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def vocalization(self):
        print(f'{self.name} is barking...')


# Creating the pickle file ----------------------------------------------------------------


cat = Cat('Felix')
dog = Dog('Buck')

with open('animals.pickle', 'wb') as file:  # 'wb' to write like binary data / file.
    pickle.dump((cat, dog), file)

# Reading the pickle file ----------------------------------------------------------------

with open('animals.pickle', 'rb') as file:  # 'rb' to read binary data / file.
    cat, dog = pickle.load(file)

    print(f'The cat name is {cat.name}')
    cat.vocalization()
    print(f'The cat type is {type(cat)}')

    print(f'The dog name is {dog.name}')
    dog.vocalization()
    print(f'The dog type is {type(dog)}')
