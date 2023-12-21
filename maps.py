"""
Maps - In Python are dictionaries - use {}
"""

revenue = {'jan': 100, 'feb': 200, 'mar': 300}
print(revenue)

# Iteration
print('Keys:')
for key in revenue:
    print(key)
    print('Values:')
for key in revenue:
    print(revenue[key])

# All Keys
print(f'Keys: {revenue.keys()}')

for key in revenue.keys():
    print(revenue[key])

# Access values
print(revenue.values())

# Unboxing
for value in revenue.values():
    print(value)

# Sum, Max Value, Min Value, Length

print(f'Sum: {sum(revenue.values())}')
print(f'Max Value: {max(revenue.values())}')
print(f'Min Value: {min(revenue.values())}')
print(f'Map Length: {len(revenue.values())}')
