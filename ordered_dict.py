"""

Collection Modules: Ordered Dict

Dictionaries = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

For key, value in dictionaries.items():
    print(f'Key = {key}, Value = {value}')
"""
# ORDERED DICT

from collections import OrderedDict

dictionaries2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# With a OrderedDict we have a default ordination of datas.
for key, value in dictionaries2.items():
    print(f'Key = {key}, Value = {value}')
