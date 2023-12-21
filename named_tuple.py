""""
Collection Module: Named Tuple

Tuple = (1, 2, 3)

Print (type(tuple[1]))

Named Tuple -> Tuples where specified name and parameters

"""
from collections import namedtuple

dog = namedtuple('dog', 'age name race')

# Other Form

cat = namedtuple('cat', 'age, name, race')

# Other Forme

horse = namedtuple('horse', ['age', 'name', 'race'])

# Use

horus = dog(age=5, name='Horus', race='Border Collie')
print(horus)

# Access data

print(horus.age)
print(horus.race)
print(horus.name)

# OR

print(horus[0])
print(horus[1])
print(horus[2])
