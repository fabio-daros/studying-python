"""
Try / Except / Else / Finally

Type: When I need treated errors?
Answer: EVERY ENTRANCE OF DATA NEED BE TREATED.

"""
# Example 1 with try and Except ---------------------------------------

num_01 = 0

try:
    num_01 = int(input('Input a number: '))
except ValueError:
    print('Incorrect value!')

print(f'You informed {num_01}')

# Example 2 - Else ---------------------------------------

try:
    num_02 = int(input('Input another number: '))
except ValueError:
    print('Incorrect value!')
else:
    print(f'You informed {num_02}')

# Example 3 - Finally  ---------------------------------------

try:
    num_03 = int(input('Input more one number: '))
except ValueError:
    print('Incorrect value!')
else:
    print(f'You informed {num_03}')
finally:
    print('Finally in action... Close or deallocate the resource.')


# Type_01: The "finally:" block every time is executed.
# Type_02: Normally used to close or deallocate a resource (Example: connections with database).

# Example 4 - Complex example  ---------------------------------------
# You is responsible for all inputs, so treat!
# Correct form:

def division(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Incorrect Value!'
    except ZeroDivisionError:
        return 'Not is possible divisions for zero!'


num1 = input('Input the first number: ')
num2 = input('Input the second number: ')

print(division(num1, num2))


# Example 5 - Generic example  ---------------------------------------

def division(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'A problem has been occurred!'


num1 = input('Input another first number: ')
num2 = input('Input another second number: ')

print(f'The result of division is: {division(num1, num2)}')


# Example 6 - Semi-Generic example  ---------------------------------------

def division(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):  # Many exceptions in a tuple # GREAT TYPE!!!
        return 'A problem has been occurred!'


num1 = input('Input another first number: ')
num2 = input('Input another second number: ')

print(f'The result of division is: {division(num1, num2)}')
