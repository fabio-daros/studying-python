"""
While - Boolean Expression
    //execution of while loop

The while has been executed then the boolean expression is true

num1 = 1

while num1 <= 10:
    print(num1)
    num1 = num1 + 1
"""

"""
# Exemplar de funcao:

def get_user_confirmation():
    while True:
        answer = input('Finish process? (yes/no) ').lower()

        if answer == 'yes':
            print('Ok, process done!')
            return True
        elif answer == 'no':
            print('Ok, process continues!')
            return False
        else:
            print('Invalid input. Please try again with yes/no')
"""

while True:
    answer = input('Finish process? (yes/no) ').lower()

    if answer == 'yes':
        print('Ok, process done!')
        break
    elif answer == 'no':
        print('Ok, process continues!')
    else:
        print('Invalid input. Please try again with (yes/no)')
