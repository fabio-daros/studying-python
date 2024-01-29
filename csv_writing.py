"""
Writing in CSV Files.

Reader(), writer()

Writerow() -> write a line
"""

# Example_1: writer() generate a object to write in CSV file------------------------------------------------------------
# The writerow() write in each line.
"""
from csv import writer

with open('movies_Writer.csv', 'w') as file:  # With 'w' open and recreate the file. Use 'a'
    writer_csv = writer(file)
    movie = None
    writer_csv.writerow(['Title', 'Year', 'Rating'])  # Header
    while movie != 'exit':
        movie = input('Enter a movie title or "exit": ')
        if movie != 'exit':
            year = input('Enter a movie year or "exit": ')
            rating = input('Enter a movie rating or "exit": ')
            writer_csv.writerow([movie, year, rating])
"""

# Example_2: DictWriter() generate a object to write in CSV file--------------------------------------------------------

from csv import DictWriter

with open('movies_DictWriter.csv', 'a') as file:
    header = ['Title', 'Year', 'Rating']
    writer_csv = DictWriter(file, fieldnames=header)
    writer_csv.writeheader()
    movie = None
    while movie != 'exit':
        movie = input('Enter a movie title or "exit": ')
        if movie != 'exit':
            year = input('Enter a movie year or "exit": ')
            rating = input('Enter a movie rating or "exit": ')
            writer_csv.writerow({'Title': movie, 'Year': year, 'Rating': rating})  # Dictionary
