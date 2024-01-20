"""
OOP - Class.

1. Are blueprints or templates for creating objects. Objects are instances of classes and
represent real-world entities with:
1.1 Attributes (properties).
    1.1.1 - Represent the states for an object - know the volts, colors or the level of lumen.
2.1 Behaviors (methods).
    2.1.1 - Functions: representation of the behaviors like turn-on or turn-off.

Example: To create an automation for turn on or turn off the light bulbs of one house. Its necessary creation on class
called: "light bulb"
1 - The light bulb is an object form real-world.
2 - In Python, it is necessary to use the reserved word: class
3 - Utilizing 'pass' to use a non-finalized block.

Type_1:
- To set a name in a class is necessary (convention) to use the first letter in upper case. 'Light' or 'LightBulb'
without the '_' every in camel-case.

Type_2:
- When we are in the planning of software, we call the pre-class entity.
"""


# Example_1:

class LightBulb:  # Entity.
    pass


light_b = LightBulb()

print(type(light_b))
