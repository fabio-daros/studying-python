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

# Write json with json/pickle

import jsonpickle


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


"""
cat = Cat('Felix', 'Persian')

ret = jsonpickle.encode(cat)  # Transform in a pyObject.

print(ret)

with open('cat.json', 'w') as file:
    ret = jsonpickle.encode(cat)
    file.write(ret)
"""

# Read the file json/pickle

with open('cat.json', 'r') as file:
    content = file.read()
    ret = jsonpickle.decode(content)  # Decode from the object JSON to write.
    print(ret)
    print(type(ret))
    print(ret.name)
    print(ret.race)
