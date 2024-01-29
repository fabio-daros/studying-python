"""
Reading CSV files.

CSV_FILE = Comma Separated Values.

1. CSV files separated by commas. (1, 2, 3, 4, 5, 6, 7, 8, 9)
2. CSV files separated by semicolons. (1; 2; 3; 4; 5; 6; 7; 8; 9)
3. CSV files separated by tabs. (1\t2\t3\t4\t5\t6\t7\t8\t9)
4. CSV files separated by spaces. (1 2 3 4 5 6 7 8 9)
5. CSV files separated by commas and spaces. (1, 2, 3, 4, 5, 6, 7, 8, 9)
6. CSV files separated by semicolons and spaces. (1; 2; 3; 4; 5; 6; 7; 8; 9)
7. CSV files separated by tabs and spaces. (1\t2\t3\t4\t5\t6\t7\t8\t9)

TYPE_1: Using the following file: fighters.csv

TYPE_2: The python language has two different formats to work with CSV:
    - Reader: Permitted iteration in the lines of the CSV file like lists.
    - DictReader: Permitted iteration in the lines of the CSV file like OrderedDicts.
"""

# Example_1 - BAD FORM TO WORK WITH CSV FILES --------------------------------

"""
with open('fighters.csv') as file:
    data = file.read()
    # print(type(data))
    data = data.split(',')[2:]  # Position [2] to remove the header.
    print(data)
"""

print('Reader: ')
print('\n')

# Example_2: Reader --------------------

from csv import reader

with open('fighters.csv') as file:
    reader_csv = reader(file)
    next(reader_csv)  # Ignore the header.
    for line in reader_csv:  # Each line is a list.
        print(f'{line[0]} born in {line[1]} and measures in {line[2]} centimetres')

print('\n')

# Example_3: DictReader --------------------

print('DictReader: ')
print('\n')

from csv import DictReader

with open('fighters.csv') as file:
    reader_csv = DictReader(file)
    # next(reader_csv)  # Not necessary use to ignore the header.
    for line in reader_csv:  # Each line is a dictionary.
        print(f'{line["Name"]} born in {line["Country"]} and measures in {line["height (in cm)"]} centimetres')
