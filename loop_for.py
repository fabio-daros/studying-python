"""
Loop -> repeat structure
For -> An structure
iterables ->
- String
    name = 'Fabio Daros'
- List -> list = [1,2,3,4]
- Range -> numbers = range(1, 10)
"""
name = 'Fabio Daros'
list = [1, 2, 3, 4]
numbers = range(1, 10)

for letter in name:
    print(letter)

for number in list:
    print(number)

for number in range(1, 10):  # 0 - 9
    print(number)

for value in enumerate(name):
    print(value)

qtd = int(input('How many?'))
for i in range(1, qtd):
    print(f'print {i}')

    print('\U0001F605')
