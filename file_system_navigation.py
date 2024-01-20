"""
Files Systems and Navigation's.

To use and manipulated files from OS. Need to use the OS module.
"""
# Example_1 --------------------------
# Do import...

import os

# getcwd() -> Get the current work directory.

print(os.getcwd())

# Return the absolute directory.
"""/Users/darosfabio/PycharmProjects/guppe"""

# To change the directory, use the chdir()

os.chdir('..')

print(os.getcwd())

# Return the absolute directory one directory above. Because I use the '..'.
"""/Users/darosfabio/PycharmProjects"""

# Checking a directory - absolute or relative.

print(os.path.isabs('/PycharmProjects/'))
# True -> absolute.
# False -> relative.

# Example_2 --------------------------------
# Identify the OS with module OS:

print(os.name)  # posix (Linux and Mac), nt (Windows)

# More details:

print(os.uname())

"""
Actual return: 
posix.uname_result(sysname='Darwin', nodename='Daross-MacBook-Pro.local', release='23.2.0', 
version='Darwin Kernel Version 23.2.0: Wed Nov 15 21:54:10 PST 2023; root:xnu-10002.61.3~2/RELEASE_X86_64', 
machine='x86_64')
"""

# More details with scandir():

print(list(os.scandir('/etc')))

"""<posix.ScandirIterator object at 0x10d031060>"""

file = list(os.scandir())

print(file)

print(dir(file[0]))

print('\n')

scanner = os.scandir()  # Correct form to start. -------------------

print(file[0].inode())  # ??
print(file[0].is_dir())  # Is a directory? False.
print(file[0].is_file())  # Is a file? True.
print(file[0].is_symlink())  # Is a symbolic link?
print(file[0].name)  # File name.
print(file[0].path)  # Directory's.
print(file[0].stat())  # statistics.

scanner.close()  # Correct form to close. -------------------
