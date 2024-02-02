"""
Why Test code?

Automated tests.

--------------------------
|                        |
| Frontend and backend   |
--------------------------
|   Automated tests.     |
--------------------------

Why test your code?

    - Reducing the number of bugs in the code.
    - Guaranteed to new resources doesn't break the other parts of the code.
    - Testing ensures that fixed bugs never return.
    - Testing ensures that refactorings never create new bugs.

TDD - Test Driven Development.
    - Write the test before to start the development.
    - With TDD, first you write the test (first stage). And after, you start implementing the minimum code to work.
    - When the first test passes, the resource is considered complete.

These stages with TDD are like a mantra development. And are called like:
    - Red; -> The first execution you have an error in the color red, because the class is not implemented yet.
    - Green; -> The second step occurs when the test passes.
    - Refactor; -> The last step, you write the code with the best possible form.
"""


# Example_1: ------------------------------------------------------------------------------------------------

class Cat:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def vocalization(self):
        print(f'Meow meow meow... {self.name}')


# With TDD, first you write the test, like the next lines. And after, you start implementing the class.

cat = Cat('Felix')

cat.vocalization()

print(cat.name)
