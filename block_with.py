"""
The With block.

Steps to work with archives:

# 1. Open de archive.
# 2. Manipulate the archive.
# 3. Close the archive.

The With block is utilized to create a context of work.
The resources are closed beside the with block.
"""

# Example_1 - The With Block ------------------------- *** PYTHONIC FORM OF WORK WITH ARCHIVES. ***

with open('text.txt') as archive:
    print(archive.readlines())
    print(archive.close())

# print(archive.read()) -> Do not work.
# print(archive.close()) -> Do not work.
