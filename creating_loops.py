"""
Creating personal loops

"""


# Example_1 ------------------------------------------------------

def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


my_for('Testing my personal loop.')

# Example_2 ------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 8]

my_for(numbers)
