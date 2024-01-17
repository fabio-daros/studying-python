"""
Reading Files with Python

1. To read an archive in Python can be utilizing the integrated function open()

About open()
-> Simple form: only one enter parameter, in this case, utilizing the way to read the archive.
-> This function returns a _io.TextIOWrapper.

To more:
------------------------------------------------
Https://docs.python.org/3/library.functions.html
------------------------------------------------
Type_1: The function "open()", open the archive to be read. If the archive doesn't exist, the Python shows:
FileNotFoundError

<_io.TextIOWrapper name='text.txt' mode='r' encoding='UTF-8'>

"mode=r" -> Reade mode. - read().
"encoding='UTF-8'" -> 99% of the cases.

"""

# Example_1 - Read from a file call text.txt in this principal directory -------------------------------------------

archive = open('text.txt')

# print(archive)

# print(type(archive))

"""To read an archive, need use the function read()"""

print(archive.read())

"""
Type_2: Its necessary open() and read()

If I try open() again, nothing can read(), because the Python use an cursor to indicate the position of the code 
and the open was executed in the start of the module.
"""
"""
Type_3: All content of the archive "text.txt" is read.
"""
