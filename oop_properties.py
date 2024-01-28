"""
OOP - Properties

1. Use the getter and setters methods.
2. In Java, it is necessary to create a public methods in the classes to manipulate the attributes.
This method is called for getters and setters.
3. Getters: Return the value of the attribute property.
4. Setters: Set the value of the attribute property.
5. To create a getter in Python, its necessary creation of the @property to use like a getter.
6. To create a setter in Python, its necessary creation of the special property or: @limit.setter
7. It's possible to create methods in Python like property.

Type_1:
 - Attention to the setters, because this method has the power to modify the information.
"""


class Account:
    counter = 400

    def __init__(self, holder, balance, limit):
        self.__number = Account.counter  # Encapsulating
        self.__holder = holder  # Encapsulating
        self.__balance = balance  # Encapsulating
        self.__limit = limit  # Encapsulating
        Account.counter += 1

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter  # Special property.
    def limit(self, new_limit):
        self.__limit = new_limit

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
    def total_value(self):
        return self.__balance + self.__limit


# Sum every accounts: ------------------------------
# LIKE JAVA LANGUAGE: Using getters and setters in the function.

"""
Example:

    def get_number(self):
        return self.__number

    def get_holder(self):
        return self.__holder

    def set_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def get_limit(self):
        return self.__limit

    def set_limit(self):
        return self.__limit


sum_1 = account_1.get_balance() + account_2.get_balance()
print(f'The sum of the accounts is: {sum_1}')

print(account_1.__dict__)
account_1.set_limit(9999999)
print(account_1.__dict__)
"""
# Sum every accounts: ------------------------------
# IN PYTHON: To getters and setters we use decorators called: @property's.
# Type_2: Create the @property's under the constructor method -> like this example.
"""
Example:

  @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit
"""

account_1 = Account('John', 3000.00, 5000.00)
account_2 = Account('Beth', 10000.00, 15000.00)

print(account_1.extract())
print(account_2.extract())

# Sum every accounts: ------------------------------
# @property is an getter.

sum_1 = account_1.balance + account_2.balance  # only the word "balance" is the @property.

print(f'The sum of the accounts is: {sum_1}')

# To create a setter in Python, we need to create a specific setter or: @limit.setter
"""
Example:
    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit
"""

# Testing:

print(account_1.__dict__)
account_1.limit = 7886.00
print(account_1.__dict__)
print(account_1.limit)

# It's possible to create methods in Python like property's.

print(account_1.total_value)  # The total_value is a property, not a function.
print(account_2.total_value)  # The total_value is a property, not a function.
