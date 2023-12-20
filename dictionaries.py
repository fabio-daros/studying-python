"""
Dictionaries or Maps

PS1: Dictionaries are collections type key/value.

PS2: Dictionaries are represented for keys {}

PS3: key/value can be used with many types of data.
"""

my_dict = {'a': 1, 'b': 2, }
print(type(my_dict))

print('Dict creation: Form 1')
# Dict creation: Form 1
countries = {'br': 'Brazil', 'fr': 'France', 'eua': 'United States'}
print(countries)
print(type(countries))

print('Dict creation: Form 2')
# Dict creation: Form 2
countries = dict(br='Brazil', fr='France', eua='United States')
print(countries)
print(type(countries))

# Access Elements with keys
print('Access Elements with keys')

print(countries['br'])
print(countries['fr'])
# print(countries['ru'])  # -> With one access with an existent key, we have a keyError.

# Access Elements with get - Recommended
print('Access Elements with get "var.get" - Recommended')

print(countries.get('br'))
print(countries.get('fr'))
print(countries.get('ru'))  # With .get, don't have an error only a "None".
# The type None are usable when we need start a var without a type and always be 'False'.

# treatment(without var.get)
if 'eua' in countries:
    print(f'Found {countries}')
else:
    print(f'Not found {countries}')

countries_new = {'br': 'Brazil', 'fr': 'France', 'eua': 'United States'}

countries_new = countries_new.get('ru', 'Not Found')  # Default value
print(f'Found: {countries_new}')

countries_new2 = {'br': 'Brazil', 'fr': 'France', 'eua': 'United States'}

print('br' in countries_new2)
print('ru' in countries_new2)
print('United States' in countries_new2)  # Validate with a key exists in a dict
# We can use anytype of data (int, float, string, boolean), lists, tuples, and dictionaries to keys

print('Another form to create dictionary:')

locations = {
    (55.6895, 39.6917): 'Brazil',
    (35.7128, 74.0064): 'New York',
    (37.6674, 98.5675): 'Tokio'
}
print(locations)
print(type(locations))

# ADD elements

revenue = {'jan': 100, 'feb': 120, 'mar': 300}
print(revenue)
print(type(revenue))

# Form 1 -> More common
revenue['apr'] = 350
print(revenue)

# Form 2

new_revenue = {'may': 500}
revenue.update(new_revenue)
print(revenue)

# Update datas in one dictionary

# Form 1

revenue['may'] = 550
print(revenue)

# Form 2

revenue.update({'may': 600})
print(revenue)

# 1 - Add or updates are the same thing.
# 2 - Dicts Not accept equals keys.

# Remove Datas

# Form 1
print('Remove Datas with pop: mar')
revenue.pop('mar')
print(revenue)
# Necessary inform the key. If the key does not exist, a KeyError return
print('Remove Datas with del: feb')
del revenue['feb']
print(revenue)

"""
Where I can use dictionaries?
1 - A cart from a web store
    Example: Cart:
    Product 1
        - name
        - quantity
        - price
    Product 2
        - name
        - quantity
        - price       
"""

cart = []

product_1 = ['PlayStation 5', 1, 2300.00]  # List
product_2 = ['God of War - Game', 2, 350.00]  # List

cart.append(product_1)
cart.append(product_2)

print(cart)
print(f'Description product: {cart[0][0]}')
print(f'Quantity: {cart[0][1]}X')
print(f'Price: {cart[0][2]} EU')
print(f'Description product: {cart[1][0]}')
print(f'Quantity: {cart[1][1]}X')
print(f'Price: {cart[1][2] + cart[1][2]} EU')
total_quantity = (cart[0][1] + cart[1][1])
total_price = (cart[0][2] + cart[1][2] + cart[1][2])
print(f'Total Quantity: {total_quantity}X')
print(f'Total Price: {total_price} EU')

"""
Methods from dictionary
"""

d = dict(a=1, b=2, c=3)
print(d.keys())
print(d.values())

# Clear Dict
d.clear()
print(d)

# Copy a dic to other (Deep Copy)

d_new = d.copy()
print(d_new)

d_new['d'] = 4  # Deep Copy

print(d)
print(d_new)

# Copy a dic to other (Shallow Copy)

d_new2 = d_new
print(d_new2)

d_new2['e'] = 5  # Shallow Copy

print(d_new)
print(d_new2)
