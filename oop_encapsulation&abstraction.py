"""
OOP - Encapsulation and Abstractions.

Type_1:
The great objective of OOP is to encapsule the code inside the hierarchic logic group utilizing class...

Encapsule -> Capsule.
Example:
            Class
-------------------------------
|____Attributes and methods___|
|_____________________________|

Remembering:
Attributes and Methods in Python

Imagine that the code has a class call: "Person:", containing a private attribute call __name and a private methode
call: "__speak()"...

This private element must be only inside the class.
But the Python doesn't block this access outside the class.
Occurred a phenomenon called Mangling.
Mangling -> Permits an alteration to access the private elements:
Example:
    _Class__element

To access private elements outside the class.:
    Instance._Person__name

    Instance._Person__speak()

Abstraction:
In OOP is the act to expose only the relevant data in a class, hiding private attributes and methods from the user.

"""


class Account:
    counter = 400

    def __init__(self, holder, balance, limit):
        self._Account__holder = None
        self.__number = Account.counter  # Encapsulating
        self.__holder = holder  # Encapsulating
        self.__balance = balance  # Encapsulating
        self.__limit = limit  # Encapsulating
        Account.counter += 1

    def extract(self):
        print(f"Balance of {self.__balance} of the {self.__holder} limit's: {self.__limit}")

    def deposit(self, value):  # Only example.
        if value > 0:
            self.__balance += value
        else:
            print('The value to deposit need to be positive.')

    def withdraw(self, value):
        if value > 0:
            if self.__balance >= value:
                self.__balance -= value
            else:
                print(f'Insufficient balance to withdraw')
        else:
            print('The value to withdraw need to be positive.')

    def transfer(self, value, destination_account):
        self.__balance -= value  # 1. Remove the value from the origin account.
        self.__balance -= 20  # Fee of transfer.
        destination_account.__balance += value  # 2. Add the value in the destination account.

    @property
    def Account__holder(self):
        return self._Account__holder


# Testing:

account_1 = Account('Buck', 200.00, 1500.00)

print(account_1.__dict__)

account_1.extract()

print(account_1.Account__holder)  # Name Mangling

"""
ATTENTION!! 
If a system with this bad form of implementation goes into production all can be altered and the 
security goes down the water:

Example:


account_1.number = 42

account_1.holder = 'Somebody'

account_1.balance = 999999999999999999999

account_1.limit = 9999999999999999999999999999

print(account_1.__dict__)


To refactoring this problem, is necessary transform the attributes publics in privates:

Example in the constructor method:

    def __init__(self, holder, balance, limit):
        self.__number = Account.counter
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        Account.counter += 1
 
"""

# Testing the Methods:

account_1.deposit(380)

print(account_1.__dict__)

account_1.withdraw(200)

print(account_1.__dict__)

# Creating a second account:

account_2 = Account('Astrid', 300.00, 2000.00)
account_2.extract()

account_2.transfer(100, account_1)  # transfer operation.

account_1.extract()

account_2.extract()
