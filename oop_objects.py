"""
OOP - Objects

1. There Are instances a class.
2. Represents an object from the real world.
3. Create how many are necessary.
4. Are variables of a defined type in the class.
"""


class BulbLight:
    def __init__(self, color, voltage, lumen):  # Constructor Method.
        self.__color = color
        self.__voltage = voltage
        self.__lumen = lumen
        self.light_on = False  # method default

    def check_bulb_light(self):
        return self.light_on

    def on_off(self):
        if self.light_on:
            self.light_on = False
        else:
            self.light_on = True


class Client:

    def __init__(self, name, document):
        self.__name = name
        self.__document = document

    def saying(self):
        print(f'The client {self.__name} say hello!')


class CurrentAccount:
    counter_cc = 4999

    def __init__(self, limit, balance, client):
        self.__number = CurrentAccount.counter_cc + 1
        self.__limit = limit
        self.__balance = balance
        self.__client = client
        CurrentAccount.counter_cc = self.__number

    def show_client(self):
        print(f'Client: {self.__client._Client__name}')


class User:
    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password


# Instance of BulbLight: / Objects
"""
lamp_1 = BulbLight('white', '110', '80')

lamp_1.on_off()  # an instance to turn on or turn off the state of lamp

print(f'The lamp on? {lamp_1.check_bulb_light()}')

current_account_1 = CurrentAccount(5000, 20000)

user_1 = User('Buck', 'Brown', 'buck.brown@email.com', '123456')
"""

# Instance of CurrentAccount: / Objects

client_1 = Client('Astrid Red', '123.456.789-00')

cc = CurrentAccount(5000, 10000, client_1)  # I pass the instanced object "client_1" like parameter to another instance.

print(cc.show_client())

cc._CurrentAccount__client.saying()  # Bad form
