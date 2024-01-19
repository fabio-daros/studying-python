"""
Open files modes

'r' -> Open to read.
'w' -> Open to write and overwrite the file.
'x' -> Open to write if the file does not exist.
'a' -> Open to write add at the final of the file (The cursor can't be controlled).
'+' -> Open to update the file (read and write).
"""

# Example_1 - Use of 'x' ---------------------------

try:

    with open('new_text_3.txt', 'x') as archive:
        archive.write('Test of content.\n')
        archive.write('Using the mode x...')

except FileExistsError:
    print('This file already exists, Try another name.')

"""
If the file exist -> Error
/usr/local/bin/python3.12 /Users/darosfabio/PycharmProjects/guppe/open_files.py 
Traceback (most recent call last):
  File "/Users/darosfabio/PycharmProjects/guppe/open_files.py", line 11, in <module>
    with open('new_text_3.txt', 'x') as archive:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileExistsError: [Errno 17] File exists: 'new_text_3.txt'
"""

# Example_2 - Use of 'a' -------------------------------
# Most interesting.

with open('fruits_from_user.txt', 'a') as archive:
    while True:
        fruit = input('Enter the name of a fruit or exit: ')
        if fruit != 'exit':
            archive.write(fruit)
            archive.write('\n')
        else:
            break

# Example_3 - Use of 'r+' to take the control cursor -------------------------------

with open('fruits_from_user.txt', 'r+') as archive_1:
    while True:
        fruit = input('Enter the name of a fruit to add at the top of the file or enter exit: ')
        if fruit != 'exit':
            archive_1.write(fruit)
            archive_1.write('\n')
        else:
            break
