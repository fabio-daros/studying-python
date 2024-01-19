"""
Write in files.

1. It's necessarily open in another format, because when an archive is open to read, it is not possible to write in
there. Only read. If open an archive t write, it is not possible to read, only write.
"""

# Example_1 - Write -----------------------------

with open('new_text.txt', 'w') as archive:  # 'w' -> write mode (only difference of open).
    archive.write('Is very easy write in archives.\n')
    archive.write('We can add the number of lines necessary.\n')
    archive.write('This is the last line.\n')
    # When add another new line, the original archive is replaced.
    archive.write('More one line...')

# Example_2 Write the word: 'Hello' 1000x ------------------------------

with open('new_text_2.txt', 'w') as archive_2:
    archive_2.write('Hello\n' * 1000)

# Example_3 Receive datas from user ------------------------------

with open('fruits_from_user.txt', 'w') as archive_3:
    while True:
        fruit = input('Enter the name of a fruit or exit: ')
        if fruit != 'exit':
            archive_3.write(fruit)
            archive_3.write('\n')
        else:
            break
