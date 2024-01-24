"""
OOP - Methods.

1. Methods are functions and are representative form of behavior of an object.
2. In Python, the methods are divided in two groups:
    2.1. Methods of instances.
    2.2. Methods of class.

Type_1:
 - The method dunder init: '__init__' is a special method called constructor.
 - The function of the method dunder init is build the object from the class.

Type_2:
 - All elements in python started in '__' and finish in '__' are called dunder (Double Underline)

Type_3:
 - The methods/functions dunder in Python are called too: Magic Methods.

Type_4: ATTENTION!
 - As much as we can create our own functions using dunder, this creation is not advisable. Python
has several methods with this form of naming, and we can change some behavior of an existing function.
"""
from passlib.hash import pbkdf2_sha256 as cryp


# Example_1 ------------------------------------------------
# Creating an Bulb Light.

class BulbLight:
    def __init__(self, color, voltage, lumen):  # Constructor Method.
        self.__color = color
        self.__voltage = voltage
        self.__lumen = lumen


class CurrentAccount:
    counter_cc = 4999

    def __init__(self, limit, balance):
        self.__number = CurrentAccount.counter_cc + 1
        self.__limit = limit
        self.__balance = balance
        self.light_on = False


class Product:
    counter_p = 0

    def __init__(self, name, description, value):
        self.__id = Product.counter_p + 1
        self.__name = name
        self.__description = description
        self.__value = value
        Product.counter_p = self.__id

    def discount(self, percentage):
        """Return the value of the product with discount."""
        return (self.__value * (100 - percentage)) / 100


class User:
    counter_u = 0

    @classmethod  # Class method or Static method -> Anyone attribute is access.
    def counter_users(cls):  # cls is the own class(Python Convention).
        print(f'{cls.counter_u} user(s) logged.')

    @classmethod  # Class method or Static method -> Anyone attribute is access.
    def see(cls):
        print('Teste')

    @staticmethod  # Only static method the decorator is different.
    def definition():
        return 'UXR344'

    def __init__(self, first_name, last_name, email, password):
        self.__id = User.counter_u + 1
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = cryp.hash(password, rounds=200000, salt_size=16)
        User.counter_u = self.__id
        print(f'Created user: {self.__generate_user()}')

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    def check_password(self, password):
        if cryp.verify(password, self.__password):
            return True  # In case the password match.
        return False

    def __generate_user(self):  # Private Methods
        return self.__email.split('@')[0]


""" 
Type_4: ATTENTION! -> Example.
    def __run__(self, meters):
        print(f'{self.__name} are running {meters} meters.')
"""

# Testing_1: ---------------------------------------------------------------------------------
"""
product_1 = Product('Fridge', 'Electronics', 2300)

print(product_1.discount(50))  # 50% of discount
"""
# Testing_2: ---------------------------------------------------------------------------------
"""
user_1 = User('John', 'Marston', 'john.marston@email.com', '12345678')

user_2 = User('Arthur', 'Morgan', 'arthur.morgan@email.com', '87654321')

print(user_1.full_name())

print(user_2.full_name())
"""
# Testing_3: ---------------------------------------------------------------------------------
# Install a external library to cryptography the password of the User.
# "pip install passLib"
"""
first_name = input('Enter your first name: ')

last_name = input('Enter your last name: ')

email = input('Enter your email: ')

password = input('Enter your password: ')

password_confirm = input('Enter your password again to confirm: ')

if password == password_confirm:
    user = User(first_name, last_name, email, password)
else:
    print('Passwords dont match...')
    exit(42)  # Process finished with exit code 42

print('User created with success!')

password = input('Enter your password to access: ')

if user.check_password(password):
    print('Access permitted.')
else:
    print('Invalid password!')

print(f'Password user cryptographic:  {user._User__password}')  # Wrong access.
"""
# Methods of Class. ---------------------------------------------------------------------------------------------------
# Need use decorator.
"""
user_1 = User('Mary', 'Jane', 'mary.jane@email.com', '123456')

User.counter_users()  # Correct form.
"""

# Private Methods ---------------------------------------------------------------------------------------------------
# Executed only inside the class

"""
user_3 = User('John', 'Marston', 'john.marston@email.com', '123456')

# print(user_3._User__generate_user()) # Bad form.
"""

# Statics Methods ---------------------------------------------------------------------------------------------------
"""
print(User.counter_u)

print(User.definition())

user = User('Arthur', 'Morgan', 'arthur.morgan@email.com', '123456')  # instance from an object.

print(user.counter_u)

print(user.definition())
"""
