"""
Study Conditionals

if conditional
else conditional
elif conditional

"""

try:
    age = int(input('Enter your age: '))

    if age < 0:
        print("Please enter a valid age greater than or equal to 0.")
    elif age < 16:
        print("You are underage.")
    elif age == 16:
        print("You just turned 16 and are now of legal age.")
    else:
        print("You are of legal age.")

except ValueError:
    print("Please enter a valid integer for your age.")
