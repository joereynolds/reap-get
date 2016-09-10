import unittest
import sys


import user


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = user.User('test_fixtures/test_user.json')

    def test_it_returns_a_property(self):
        expected = 'win32'
        actual = self.user.get_property('os')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
