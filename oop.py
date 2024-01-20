"""
Object-oriented programming - OOP

OOP stands for Object-Oriented Programming. It is a programming paradigm that uses objects, which are instances of
classes, to design and organize code. In object-oriented programming, the key concepts include:

Classes and Objects:
Classes are blueprints or templates for creating objects. Objects are instances of classes and
represent real-world entities with:
1. Attributes (properties)
2. Behaviors (methods).

Encapsulation:
Encapsulation refers to the bundling of data (attributes) and the methods that operate on that data
within a single unit or class. It helps in hiding the internal details of an object and exposing only what is necessary.

Inheritance:
Inheritance allows a class (subclass or derived class) to inherit properties and behaviors from another
class (superclass or base class). It promotes code reuse and establishes a relationship between classes.

Polymorphism:
Polymorphism allows objects of different classes to be treated as objects of a common base class. It
enables methods to be called on objects without knowing their specific types, providing flexibility and extensibility.

Object-oriented programming is widely used for designing and implementing software due to its ability to model
real-world entities, enhance code organization, and facilitate code reuse and maintenance. Popular programming
languages that support OOP include Java, C++, Python, and many others.
"""

# To start:


number = 10
print(number)
print(type(number))
# <class 'int'>

name = 'Name'
print(name)
print(type(name))


# <class 'str'>


class Product:
    pass


ps5 = Product()
print(ps5)
# Allocated a space on the memory to the use: <__main__.Product object at 0x10dbe9f10>
print(type(ps5))
# <class '__main__.Product'> Now the variable 'ps5' have a new type or the type of the class -> Product.
