import unittest
from count_vowels import count_vowels


class count_vowelsTest(unittest.TestCase):

    def test_input_str(self):
        self.assertEqual(count_vowels(int), "invalid input")
