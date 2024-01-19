"""
File System - Manipulations.

Documentation:
https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
import os

# 1. Discover if a file or a directory exists.

print(os.path.exists('text.txt'))  # True. Because the file exists.

# Relative Paths - Without the '/'
print('Relative Paths: ')
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('Example'))  # False

# Absolute Paths
print('Absolute Paths: ')
print(os.path.exists('/home/geek/university'))  # False
print(os.path.exists('/Library/ColorPickers'))  # True

# Creating files

# Form 1:
open('creating_file_w.txt', 'w').close()

# Form 2:
open('creating_file_a.txt', 'a').close()

# Form 3:
with open('creating_file_pass.txt', 'w') as file:
    pass  # Pass -> do not everything. Only to add anything in the block.

# Form 4 -> BEST FORM:
"""
os.mknod('creating_file_mknod.txt')  # If the file can be existed, an error FileExists occurred.

os.mknod('/Users/PycharmProjects/guppe/creating_file_mknod_absolute.txt')
"""

# Creating unique directory. 1 by 1...
"""
os.mkdir('templates')
"""

# Creating multi or tree directory's...
"""
os.makedirs('dir_created_by_python/dir_1/dir_2')  # If exists -> FileExistsError:
"""

# Creating multi or tree directory's with condition...
"""
os.makedirs('dir_created_by_python/dir_1/dir_2', exist_ok=True)  # If exists -> ignore.
"""
# Rename.
"""
os.rename('dir_created_by_python', 'dir_created_by_python_renamed')

os.rename('dir_created_by_python_renamed/dir_1/dir_2', 'dir_created_by_python_renamed/dir_1/dir_1.1')
"""
# Rename File.
"""
os.rename('fruits_from_user.txt', 'fruits_from_user_renamed.txt')
"""

# Delete file: ATTENTION THE DELETE IS DEFINITELY.

os.remove('new_text.txt')

# Only to create again. ------------------------------
with open('new_text.txt', 'w') as archive:
    pass
# Only to create again. ------------------------------

# Delete empty dirs:
"""
os.rmdir('dir_created_by_python/dir_1/dir_2')
"""
# If the directory doesn't empty, an OSError occurred.
# If the directory doesn't exist, a FileNotFoundError occurred.

# Delete all content or a Tree dirs:
for file in os.scandir('dir_created_by_python'):
    if file.is_file():
        os.remove(file.path)
    if not file.is_file():
        os.rmdir(file.path)

# Delete a Tree of empty dirs:
"""
os.remove('dir_created_by_python')
"""

# Send files to trash.
# Need to install an external library: "pip install send2trash"
# Import:
"""
from send2trash import send2trash

send2trash('fruits_from_user_renamed.txt')  # If the file does not exist -> OSError: File not found
"""

# creating a temp directory.
"""
import os
import tempfile

with tempfile.TemporaryDirectory() as temp:  # with to create a directory.
    print(f'Directory created in: {temp}')
    with open(os.path.join(temp, 'temp_file_python.txt'), 'w') as file:  # with to create a file.
        file.write('Hello World from new temp file\n')
    input()
"""
# When the code finishes the 'with', the file is destroyed.

# Another example to creating a temp directory.
# Without the with block.

import tempfile

file = tempfile.TemporaryFile()
file.write(b'Hello World from Python\n')
# 'b' -> This 'tempfile.TemporaryFile' needs bytes to write. and don't use 'f' -> string
file.seek(0)
print(file.read())
file.close()  # Necessary close the writing because I don't use the 'with'.
