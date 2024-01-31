"""
JSON and Pickle

JSON: JavaScript Object Notation

API: They are forms of communication between services offered by companies (X, Facebook, YouTube...) and thirds
"""
# Example_1: ----------------------------------------------------------------
"""
import json

ret = json.dumps(['products', {'PlayStation 5': ('2TB', 'New', '110V', 2500.00)}])  # JSON use: " "

print(type(ret))

print(ret)

"""
# Example_2: ----------------------------------------------------------------
"""
class Cat:
    def __init__(self, name, race):
        self.__name = name
        self.__race = race

    @property
    def name(self):
        return self.__name

    @property
    def race(self):
        return self.__race

cat = Cat('Felix', 'Persian')

print(cat.__dict__)  # Simple blades.

ret = json.dumps(cat.__dict__)  # JSON format: Use quotation marks.

print(ret)
"""

# Integration JSON and Pickle ----------------------------------------------------------------
# pip install jsonpickle
