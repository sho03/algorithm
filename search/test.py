import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):


  def test_binary_search(self):
    target = 7
    a = [1,2,5,7,10,20,100]
    self.assertEqual(binary_search.binary_search(a, target), True)
  
  def test_binary_search2(self):
    target = 8
    a = [1,2,5,7,10,20,100]
    self.assertEqual(binary_search.binary_search(a, target), False)
  
if __name__ == '__main__':
  unittest.main()