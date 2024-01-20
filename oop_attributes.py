"""
OOP - Attributes.

1. Representative the characteristics of the object.
2. In Python, we are dividing the attributes in three groups:
    2.1. Instances;
    2.2. Class;
    2.3. Dynamics;

Type_1: Constructor methods: Special methode to construct an object.

Type_2: self. -> Is the object that executes the method.
"""


# Attribute of instances Publics: Declared inside constructor methode. ------------------------------------------------
# To start:

class LightBulb:
    def __init__(self, voltage, color):  # The 'self' used here is a convention. # __init__ -> constructor method.
        self.voltage = voltage  # method
        self.color = color  # method
        self.light_on = False  # method


class CurrentAccount:
    def __init__(self, number, limit, balance):
        self.number = number
        self.limit = limit
        self.balance = balance


class Product:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


"""
Type_3: 
Attributes publics and privates:
    1. Private: The access occurred only inside the class.
    2. Public: The access occurred in all parts of the project (Global).

Type_4: 
In Python every attribute from a class is public (Convention).

Type_5: 
In case of an attribute can need be private, we use '__' or 'Name Mangling'.
Example: 
'self.__name = name'
"""


# Attribute of instances Privates:

class Access:
    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def show_password(self):
        print(self.__password)

    def show_email(self):
        print(self.email)


user = Access('username@email.com', '123456')

print(user.email)

# print(user.__password)  # AttributeError: 'Access' object has no attribute '__password'

print(user._Access__password)

user.show_password()
user.show_email()

# Instances attributes:
# All instances/objects have the same attribute.
# Example:

user_1 = Access('user_1@email.com', '123456')
user_2 = Access('user_2@email.com', '654321')

user_1.show_email()
user_2.show_email()


# Class attribute: -----------------------------------------------------------------------------------------------------
# Attributes declared inside the class, outside the constructor.
# Example_1:
# Refactoring the Product class.
class ProductNew:
    tax = 1.05  # Class attribute - 0.05% of tax -> All products receive this tax value.
    counter = 0

    def __init__(self, name, description, value):
        self.id = ProductNew.counter + 1  # Don't have in the constructor.
        self.name = name
        self.description = description
        self.value = value
        ProductNew.counter = self.id  # To update the id.


p_1 = ProductNew('Play Station 5', 'Console', 2300)
p_2 = ProductNew('XBox Series X', 'Console', 4500)

# Incorrect form to access an attribute from a class.
print(p_1.tax)
print(p_2.tax)
# Same value to p_1 and p_2 because de tax is from class.

# Incorrect form to access an attribute from a class.
print(p_1.value)
print(p_2.value)
# Different value to p_1 and p_2 because de value is from instance.

# The correct form to access an attribute of class:
print(ProductNew.tax)  # 1.05

# To see the increment of the id.
print(p_1.id)
print(p_2.id)

"""
Type_6:
In another languages like Java, the attributes of class are called static attributes.
"""

# Dynamic attribute: -------------------------------------------------------------------------------------------------
# Instance attribute created in execution time.
"""
Type_7:
The dynamic attribute is exclusive of the instance that create it.
"""

product_1 = ProductNew('Fridge', 'Electronics', 5000)

product_2 = ProductNew('Television', 'Electronics', 3500)

# created in execution time.

product_2.weight = '35kg'  # The attribute 'weight' don't exist in the ProductNew class.

print(
    f'Product: {product_2.name},\n'
    f'Description: {product_2.description},\n'
    f'Value: {product_2.value},\n'
    f'Weight: {product_2.weight} -> This is an dynamic attribute.'  # Dynamic attribute.
)
"""
print(
    f'Product: {product_1.name},\n'
    f'Description: {product_1.description},\n'
    f'Value: {product_1.value},\n'
    f'Weight: {product_1.weight} -> This is an dynamic attribute.'  # Dynamic attribute.
)
# AttributeError: 'ProductNew' object has no attribute 'weight' Because I don't generate a dynamic attribute.
"""

print(product_1.__dict__)  # __dict__ to see the property of the attribute.
# {'id': 3, 'name': 'Fridge', 'description': 'Electronics', 'value': 5000}
print(product_2.__dict__)
# {'id': 4, 'name': 'Television', 'description': 'Electronics', 'value': 3500, 'weight': '35kg'}


# __dict__ to see info's of the class:
print(ProductNew.__dict__)

# Dynamic delete attributes: -------------------------------------------------------------------------------------------
# Deleting the 'weight' from product_2.

del product_2.weight  # Now I don't have more the weight.

print(product_1.__dict__)
print(product_2.__dict__)  # Now I don't have more the weight.
