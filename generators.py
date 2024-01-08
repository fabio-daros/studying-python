"""
Generator Expression

At the last studies, I see:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

But I don't see:
- Tuple Comprehension

Why?

Why the real name is: GENERATORS.
"""
from sys import getsizeof

# Example 1 ---------------------------------------------
# Using Generators:

names = ['John', 'Smith', 'Carl', 'Astrid', 'Buck', 'Cris']

print(any(name[0] == 'C' for name in names))

# Example 2 ---------------------------------------------
"""
Type: Not is a list. But a Generator -> To be a list writ: print([any(name[0] == 'C' for name in names]))
"""
# Using List Comprehension:

res = [name[0] == 'C' for name in names]
print(type(res))

# Using Generators:

res = (name[0] == 'C' for name in names)
print(type(res))

"""
Type: Generator have more performance than lists.
"""

# Import from sys with "gets sizeof"
# To show the number of bytes a string occupied in memory.
# Tests:

print(getsizeof('Hello World'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(2348320842309840))

print(getsizeof(True))

# Generate a list of numbers with list comprehension (To compare the space used in memory):
list_comp = getsizeof([x * 10 for x in range(1000)])

# Generate a list of numbers with Set comprehension (To compare the space used in memory):
set_comp = getsizeof({x * 10 for x in range(1000)})

# Generate a list of number with list comprehension (To compare the space used in memory):
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generate a list of number with GENERATOR (To compare the space used in memory):
gen = getsizeof(x * 10 for x in range(1000))

print('To do the same service, we used in memory:')

print(f'With List Comprehension: {list_comp} bytes')

print(f'With Set Comprehension: {set_comp} bytes')

print(f'With Dictionary Comprehension: {dic_comp} bytes')

print(f'With Generator Comprehension: {gen} bytes')

# Example 3 ---------------------------------------------
# iterations:

gen_new = (x * 10 for x in range(1000))
print(gen_new)
print(type(gen_new))

for num in gen_new:
    print(num)
