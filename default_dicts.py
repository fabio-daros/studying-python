""""
Collection Modules - Default Dictionaries

Default dict

1 - Create a dictionary with default dicts, a default value is informed and utilized as a lambda
or funtion without a name and can receive a parameter and return values

"""
from collections import defaultdict

dictionary = {'course': 'Python'}
print(dictionary)
print(dictionary['course'])

dictionary = defaultdict(lambda: '0')
dictionary['course'] = 'Python developers'
print(dictionary)
# Add more element
print(dictionary['other'])  # KeyError to dictionary common, but not here =).
print(dictionary)
