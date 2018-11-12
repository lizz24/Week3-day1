import unittest

from list_sum import list_sum


class Testlistsum(unittest.TestCase):
  

    def test_listsum(self):

        self.assertEqual(list_sum([1, 2, 3, [4, 6]]), 16)

    


if __name__ == '__main__':
    unittest.main()
