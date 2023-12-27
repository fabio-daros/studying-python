"""
Map

With Map, We do mapping between values to functions.

"""

import math


# Example 1 --------------------------

def area(r):
    # Calculate the area from circle with radius
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

# Example 2 --------------------------

radius = [2, 5, 7.1, 0.3, 10, 44]

areas = []

for r in radius:
    areas.append((area(r)))

print(areas)

# Form 2 - Map

areas = map(area, radius)

print(areas)
print(type(areas))

print(list(areas))

# Form 3 - Map with Lambda --------------------------

print(list(map(lambda r: math.pi * (r ** 2), radius)))

# PS When use the function map() then the first utilizing of a result, the variable restart to zero.

# Example 3 --------------------------

cities = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('San Diego', 28),
          ('London', 22)]  # Lists with tuples

print(cities)

# Now convert Degrees Celsius in Fahrenheit
# Formula: f = 9/5 * c + 32
# Lambda

c_for_f = lambda city: (city[0], (9 / 5) * city[1] + 32)

print(list(map(c_for_f, cities)))
