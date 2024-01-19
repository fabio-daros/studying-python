"""
Zip

zip() -> create an iterable object to aggregate the elements to each iterable in a pair.

"Get the first element and create tuples."
"""

# Example 1 ----------------------------------

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

zip_1 = zip(list_1, list_2, 'abc')
print(zip_1)

# Can use the zip o generate a list, tuple or a Dict.

print(list(zip_1))  # Create a list with tuple.

print(tuple(zip_1))  # lose in the memory, because be used.

print(set(zip_1))

print(dict(zip_1))

# Example 2 ----------------------------------

list_3 = [7, 8, 9, 10, 11]

zip_1 = zip(list_1, list_2, list_3)
print(list(zip_1))
# result: [(1, 4, 7), (2, 5, 8), (3, 6, 9)] -> The number 10 and 11 not used because the zip used the size of the
# minor list to create the tuples.

# Example 3 ----------------------------------
# using different iterables.

tuple_1 = 1, 2, 3, 4, 5
list_4 = [6, 7, 8, 9, 10]
dictionary_1 = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tuple_1, list_4, dictionary_1.values())

print(list(zt))

# List of tuples:

datas = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*datas)))

# Example 4 more complex ----------------------------------

test_1 = [90, 91, 78]
test_2 = [98, 89, 53]
students = ['Mary', 'John', 'Smith']

final = {data[0]: max(data[1], data[2]) for data in zip(students, test_1, test_2)}

print(final)

# Utilizing the map() function

final = zip(students, map(lambda proof_note: max(proof_note), zip(test_1, test_2)))

print(dict(final))
