"""
Duck Typing


"""


class BlackSwan:
    def __len__(self):
        return 42


book = BlackSwan()

print(len(book))

name_1 = 'Name'
list_1 = [12, 34, 55, 66]
dict_1 = {'Carl': 12, 'Mary': 34, 'Joana': 49}

print(len(name_1))

print(len(list_1))

print(len(dict_1))

# The len function is applicable to all types.

# If an object walks like a duck, behaves like a duck and flight like a duck... IS A DUCK...

# Similarly, objects should be bearable similar.
