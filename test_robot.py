import unittest

from robot import Robot


class RobotTestCase(unittest.TestCase):

    def setUp(self):
        self.megaman = Robot('Mega Man', battery=50)
        print('setUp() executed...')

    def test_recharge(self):
        self.megaman.recharge()
        self.assertEqual(self.megaman.battery, 100)

    def test_say_name(self):
        self.assertEqual(self.megaman.say_name(), 'BEEP... BEEP... I AM MEGA MAN')
        self.assertEqual(self.megaman.battery, 49, 'The battery should be in 49%')

    def tearDown(self):
        print('tearDown() executed...')


if __name__ == '__main__':
    unittest.main()
