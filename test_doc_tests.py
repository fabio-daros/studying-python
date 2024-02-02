"""
Doctests.

1. Doctests are used to test the documentation.

2. Doctests are tests we input in the docString of the function/methods Python.

"""


# Example_1: Test ----------------------------------------------------------------

def sum_1(a, b):
    """Sum the number a and b

    >>> sum_1(1, 2)  # This is a doctest. -> Test inside the documentation.
    3
    """
    return a + b


print(sum_1(3, 4))  # 7

# To execute the test in the terminal: "python3 -m doctest -v doctests.py"

"""
darosfabio@Daross guppe % python3 -m doctest -v test_doc_tests.py
7
Trying:
    sum_1(1, 2)  # This is a doctest. -> Test inside the documentation.
Expecting:
    3
ok
1 items had no tests:
    test_doc_tests
1 items passed all tests:
   1 tests in test_doc_tests.sum_1
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
"""


# Example_2: Two tests ----------------------------------------------------------------

def sum_2(a, b):
    """Sum the number a and b

    >>> sum_2(1, 2)  # This is a doctest. -> Test inside the documentation.
    3
    >>> sum_2(4, 6)
    100
    """
    return a + b


print(sum_1(3, 4))  # 7

"""
1 items had failures:
   1 of   2 in test_doc_tests.sum_2
3 tests in 3 items.
2 passed and 1 failed.
***Test Failed*** 1 failures.

"""


# Example_3: Using TDD: ----------------------------------------------------------------

def duplicate(values):
    """duplicate the values in a list.
    >>> duplicate([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicate([])
    []

    >>> duplicate(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicate([True, None])
    TraceBack (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]


"""
Trying:
    duplicate([1, 2, 3, 4])
Expecting:
    [2, 4, 6, 8]
ok
Trying:
    duplicate([])
Expecting:
    []
ok
Trying:
    duplicate(['a', 'b', 'c'])
Expecting:
    ['aa', 'bb', 'cc']
ok
Trying:
    duplicate([True, None])
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
ok
Trying:
    sum_1(1, 2)  # This is a doctest. -> Test inside the documentation.
Expecting:
    3
ok
Trying:
    sum_2(1, 2)  # This is a doctest. -> Test inside the documentation.
Expecting:
    3
ok
Trying:
    sum_2(4, 6)
Expecting:
    100
**********************************************************************
File "/Users/darosfabio/PycharmProjects/guppe/test_doc_tests.py", line 51, in test_doc_tests.sum_2
Failed example:
    sum_2(4, 6)
Expected:
    100
Got:
    10
1 items had no tests:
    test_doc_tests
2 items passed all tests:
   4 tests in test_doc_tests.duplicate
   1 tests in test_doc_tests.sum_1
**********************************************************************
1 items had failures:
   1 of   2 in test_doc_tests.sum_2
7 tests in 4 items.
6 passed and 1 failed.
***Test Failed*** 1 failures.
"""


# Example_3: ----------------------------------------------------------------
# Unexpected error...

def say_hello():
    """Say hello
    >>> say_hello()
    'hello'
    """
    return 'hello'


# If I put the: 'Hello,' with: "Hello" an error occurred, because the python test, use '' and don't use ""

def true():
    """Return true

    >>> true()
    True
    """
    return True
