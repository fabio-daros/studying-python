"""
String IO

ATTENTION: To write or read a file in the OS system, the software needs to have permission to:
    - Write -> Write in the file.
    - Read -> Read the File.

StringIO -> To read and write files in memory...
"""

# Example_1 --------------------------------

from io import StringIO

msg = 'This is only a normal string. '

# Can create a file in memory with a string insert or empty.

file = StringIO(msg)

# Now we have the file... and can be set the open to write and read files.

print(file.read())

# Write another text.

file.write('Another text.')

# And can manipulate the cursor.

file.seek(0)

print(file.read())
