"""
Type string

- example: '234', 'a' , 'True', '42.3'
-  quotation marks
-  double quotes
-  triple single quotes
"""

name = "Fabio Daros"
print(name)
print(type(name))

name2 = 'John Marston'
print(name2)
print(type(name2))

name3 = '''Mary Jane'''
print(name3)
print(type(name3))

name4 = 'Man at arms'
print(name4.upper())
print(name4.split())
print(name4[0:15])  # Slice string
print(name4[:: -1])  # Start from last element and inverse
