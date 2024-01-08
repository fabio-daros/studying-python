"""
Sets

1 - No duplicate values;
2 - No ordinate values;
3 - Access with index;

Use {} to Sets

Differences between Sets and Maps(Dicts):

1 - Dicts have keys and values;
2 - Sets have value only;

"""

# Create a set:

s = ({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repetitive values.

print(s)
print(type(s))
# In sets, repetitive values are ignored and are kicked to the set.

if 3 in s:
    print("3 is in set")
else:
    print("3 is not in set")

# IMPORTANT! - Don't have an order.

s1 = {99, 2, 34, 87, 90, 40, 60}
print(s1)

# Example

s2 = {99, 2, 34, 87, 'Hello World', True, False, 34.99}
print(s2)
print(f'Type: {type(s2)}')

# iteration
for value in s2:
    print(value)

# Interesting uses to Set.
# A list of visiting from a museum.
# Lists with repetitions

cities = ['San Francisco', 'New York', 'London', 'Florianopolis', 'San Francisco', 'New York', 'London']

print(cities)
print(len(cities))  # Show the length of all cities.

print(len(set(cities)))  # Show only cities not duplicated.

# Add Elements

s3 = {1, 2, 3}
s3.add(4)  # Add 4.
s3.add(4)  # Add 4 again -> don't show error, but don't add.
print(s3)

# Remove Elements

s3.remove(4)
print(f'Remove with 4 .remove() {s3}')

# Another form to remove:

s3.discard(3)
print(f'Remove with 3 .discard() {s3}')

# Two sets

students_python = {'Fabio', 'Dandara', 'Joao', 'Fernando', 'Daniel'}
students_java = {'Gustavo', 'Francisco', 'Joseph', 'Arthur', 'Daniel', 'Fernando'}

# One register with names uniques (with union).
print(f'students_python: {students_python}')
print(f'students_java: {students_java}')

unique1 = students_python.union(students_java)
print(f'students python and java with union: {unique1}')

# Another form (with pipe)

unique2 = students_python | students_java
print(f'students python and java with pipe: {unique2}')

# Generate a set in both courses (with intersection)

both1 = students_python.intersection(students_java)
print(f'students in both courses with intersection: {both1}')

# Generate a set in both courses (with &)

both2 = students_python & students_java
print(f'students in both courses with "&": {both2}')

# Generate a set with differences courses (with difference)

dif_python = students_python.difference(students_java)
print(f'students only in python with difference: {dif_python}')

dif_java = students_java.difference(students_python)
print(f'students only in java with difference: {dif_java}')

# Sum, MaxValue, Min Value, Length

s4 = {1, 2, 3, 4, 5}
print(s4)
print(sum(s4))
print(max(s4))
print(min(s4))
print(len(s4))
