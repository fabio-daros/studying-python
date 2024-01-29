"""
OOP - Magic Methods.

Magic Methods: All methods that use the dunder. (__X__).

Dunder init -> __init__.

Dunder = Double underscore.

Dunder repr -> Representation from an object.

Dunder str -> Representation to a final user.

Dunder len -> Size

Dunder add -> Add two objects.

Dunder mul -> Multiply two objects (string and integer).

"""


# Example_1: __repr__ ----------------------------------------------------------------

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):  # __repr__ do the representation of the object.
        return f'{self.title} by {self.author} has {self.pages} pages.'

    def __str__(self):  # __str__ do the representation of the object to a final user.
        return f'{self.title} by {self.author} has {self.pages} pages.'

    def __len__(self):  # __len__ Take the number of pages to print.
        return self.pages

    def __add__(self, other):  # __add__ Add two books.
        return f'{self} & {other}'

    def __mul__(self, other):  # __mul__ to multiply a string and a number.
        if isinstance(other, int):
            msg = ''
            for i in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Cannot possible multiplication.'


book_1 = Book('Python Rocks', 'Geek Universe', 400)
book_2 = Book('Artificial Intelligence with Python', 'Geek Universe', 350)

print(book_1)
print(book_2)

print('\n')

print(f'Number of pages in the book 1:  {len(book_1)}')
print(f'Number of pages in the book 2:  {len(book_2)}')

print('\n')

print(book_1 + book_2)

print('\n')

print(book_1 * 3)
