"""
Creating a custom iterator

Type: Like a range()
"""


class Counter:
    def __init__(self, minor, bigger):  # method with constructor -> function inside a class.
        self.minor = minor  # All functions inside a class need the self like an entered parameter.
        self.bigger = bigger

    def __iter__(self):  # To transforming in one iterable inside a function.
        return self

    def __next__(self):  # Another method to use the next() or __next__ -> Is the same.
        if self.minor < self.bigger:
            number = self.minor
            self.minor = self.minor + 1
            return number
        raise StopIteration


for n in Counter(1, 61):  # 1 - 60.
    print(n)

for n in range(1, 61):
    print(n)
