"""
OOP - Inheritance

The possibility of inheritance is the reuse and extend the codes.

Type_1:
With Inheritance from an existing class, it is possible to extend another class and this class inherits the attributes
and methods of the original class.

Example:

Client
    - first_name;
    - last_name;
    - document;
    - incomes;
Employee
    - first_name;
    - last_name;
    - document;
    - registration;

Question:
    - Exist any generic entity able to encapsulate the attributes and methods common to other entities?

Type_2:
- When a class inherits from an existing class, the inherited class is called:
    [Person]
    - Superclass.
    - Mother class.
    - Father class.
    - Base class.
    - Generic class.

- When a class inherits from another class, this is called:
    [Client and Employee]
    - Subclass.
    - Child class.
    - Grandchild class.
    - Specific class.

----------------------------------------------------------------
class Client:

    def __init__(self, first_name, last_name, document, incomes):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__document = document
        self.__incomes = incomes

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'


class Employee:

    def __init__(self, first_name, last_name, document, registration):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__document = document
        self.__registration = registration

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'


# Testing:

client_1 = Client('Astrid', 'Red', '123.456.789-10', 5000.00)
client_2 = Client('Buck', 'Brown', '123.456.789-11', 3000.00)

employee_1 = Employee('John', 'Marston', '123.456.789-12', 'JM123343')
employee_2 = Employee('Abigail', 'Miss', '123.456.789-13', 'AM7837846')

print(client_1.full_name())

print(client_2.full_name())

print(employee_1.full_name())

print(employee_2.full_name())
"""
"""
Many repetition of codes.
"""


# Refactoring:

class Person:  # Superclass
    def __init__(self, first_name, last_name, document):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__document = document

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'


class Client(Person):  # Client inherits from Person.

    def __init__(self, first_name, last_name, document, incomes):
        super().__init__(first_name, last_name, document)
        # The super constructor is how I access the superclass.
        self.__incomes = incomes


class Employee(Person):  # Employee inherits from Person.

    def __init__(self, first_name, last_name, document, registration):
        super().__init__(first_name, last_name, document)
        self._Person__first_name = None
        self.__registration = registration

    def full_name(self):
        print(super().full_name())  # super() access the attributes from the superclass.
        return f' Employee: {self.__registration} Name: {self._Person__first_name}'


client_1 = Client('Astrid', 'Red', '123.456.789-10', 5000.00)
employee_1 = Employee('John', 'Marston', '123.456.789-12', 'JM123343')

print(client_1.full_name())
print(employee_1.full_name())

# Overwritten of methods (Overriding) ---------------------------------------------------------------------------------
"""
When rewriting/reimplementing a method present in the superclass in a child class.
"""
client_2 = Client('Astrid', 'Red', '123.456.789-99', 5000.00)
employee_2 = Employee('John', 'Cotton', '123.456.789-00', 1234)

print(client_2.full_name())
print(employee_2.full_name())
