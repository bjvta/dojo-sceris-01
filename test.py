"""
Test module for FizzBuzz
"""

# UnitTest
import unittest

# Code
from code import upper_string


class TestCodeMethods(unittest.TestCase):

    def test_first_function(self):
        self.assertEqual(upper_string('foo'), 'FOO')

if __name__ == '__main__':
    unittest.main()