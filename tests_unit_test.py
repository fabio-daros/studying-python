import unittest

from activities import eat, sleep, is_funny


class TestActivities(unittest.TestCase):

    def test_eat_healthy(self):
        """Test the return health food."""
        self.assertEqual(
            eat('apple', True),
            'I eat apple, because I want be healthy.'
        )

    def test_eat_unhealthy(self):
        """Test the return unhealthy food."""
        self.assertEqual(
            eat('pizza', False),
            'I eat pizza, because you only live once.'
        )

    def test_sleep_little(self):
        """Test the sleep little"""
        self.assertEqual(
            sleep(2),
            'sleep for 2 hours.'
        )

    def test_sleep_a_lot(self):
        """Test the sleep a lot"""
        self.assertEqual(
            sleep(10),
            'sleep for 10 hours.'
        )

    def test_is_funny(self):
        # self.assertEqual(is_funny('Jim Carrey'), False)
        self.assertFalse(is_funny('Jim Carrey'))
        self.assertTrue(is_funny('Jim Carrey'), 'Jim Carrey should be funny.')
        # if True, execute the function else, the msg:.


if __name__ == '__main__':
    unittest.main()
