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
