"""
Decorators

What are decorators?

1. Decorators are functions.
2. Decorators involve wrapping another function to enhance or modify its behavior.
3. Decorators are examples of Higher Order Functions.
4. Decorators have onde own syntax, using the @ or (Syntactic Sugar)

|----------------------------------|
|         Function Decorator       |
|----------------------------------|

----------------------------------------
| |----------------------------------| |
| |        Decorated Function        | |
| |----------------------------------| |
----------------------------------------
"""


# Example_1 ---------------------------------------------------------------------------------
# Decorators like functions (NOT RECOMMEND / Without syntactic sugar)

def be_polite(function):
    def being_polite():
        print('It was a pleasure meeting you')
        function()
        print('Have a nice day!')

    return being_polite()


def greetings():
    print('Welcome!')


# Testing_1

be_polite(greetings)


# Testing_2

def rage():
    print('I HATE YOU!')


be_polite(rage)

print('\n')


# Example_2 ---------------------------------------------------------------------------------
# Decorators like functions (RECOMMEND / WITH syntactic sugar)

def be_polite_again(function):
    def being_polite_again():
        print('It was a GREAT pleasure meeting you')
        function()
        print('Have a GREAT day!')

    return being_polite_again()


@be_polite_again  # Sugar Syntax
def presentation():
    print('My name is Peter')


# Testing_1
presentation


# Testing_2
@be_polite_again
def sleep():
    print('I want sleep')


sleep

# Example_3 ---------------------------------------------------------------------------------
# Decorators in a menu from a website.

"""
|----------------------------------------------------|
| Home  |  Services  |  Products  |  Administration  |
|----------------------------------------------------|
examples:

http://www.yourcompany.com/home

http://www.yourcompany.com/services

http://www.yourcompany.com/products

http://www.yourcompany.com/admin

----------------------------------------

def check_login(request):
    if not request.user:
        redirect ('http://www.yourcompany.com/')

def home(request):
    return 'Permitted access to home'
    
def services(request):
    return 'Permitted access to services'

def products(request):
    return 'Permitted access to products'

@ check_login
def admin(request):
    return 'Permitted access to admin'
    
"""
