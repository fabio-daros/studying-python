"""
Hooks are tests or execution of tests.

Methods:

    1 - setup() -> Executed before each method of test. Is util to create instances of objects and other data.
    2 - tearDown() -> Executed ate the final of method test. Is util to delete data or close connections with *DBs

* DBs: Database's
"""

# Example_1: ----------------------------------------------------------------

import unittest


class TestModule(unittest.TestCase):

    def setUp(self):  # configs of setUp()
        pass

    def test_first(self):  # setUp() run before the test # tearDown() run after the test
        pass

    def test_second(self):  # setUp() run before the test # tearDown() run after the test
        pass

    def tearDown(self):  # configs of tearDown()
        pass
