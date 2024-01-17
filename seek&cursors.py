"""
Seek and Cursors

seek() -> Function utilized to movement the cursor in the archive.

"""
# Example_1 ------------------------------
"""
archive = open('text.txt')

print(archive.read())

print(archive.read())
"""
# Don't execute two times.

"""if an archive open() has update the new content not be read."""

# Moving the cursor around the file with seek()
"""
archive.seek(0)  # seek(0) -> Initial point of an archive.

print(archive.read())
"""
# Example_2 --------------------------
"""
archive = open('text.txt')

archive.seek(20)  # Start at the position (20)

print(archive.read())
"""
# Example_3 readline() --------------------------
"""
archive = open('text.txt')

ret = archive.readline()
"""
# Example_4 readlines() --------------------------
"""
archive = open('text.txt')

lines = archive.readlines()

print(len(lines))
"""
# Example_5 --------------------------
"""Type_1: When opine an archive with the function "open()" is create a connection between the archive and the computer 
disk and the program is call streaming... its necessary close the teh connection with "close()"
steps:
1 - Open archive.
2 - Work in the archive.
3 - Close the archive.
"""
# 1 - Open archive:
archive = open('text.txt')

# 2 - Work in the archive:
print(archive.read())

# 3 - Close the archive:
archive.close()
