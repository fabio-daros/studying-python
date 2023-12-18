print("Your Name?")
name = input()
print('Welcome %s' % name)
print("Your Age?")
age = int(input())
print('%s, You have %s years old' % (name, age))  # antique form
print(f'Your name is {name} and you are {age}')  # new form
print(f'The {name} have {age} years old')  # look, handsome
print(f'The {name} born in {2023 - age}')
