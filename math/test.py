import unittest
from learn_math import *

class TestMath(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(113), True)

  
if __name__ == '__main__':
  unittest.main()