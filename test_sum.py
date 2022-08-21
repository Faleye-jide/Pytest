import unittest
import argparse
from list_sum import sum

class TestSum(unittest.TestCase):
    
    data = [1,2,3,4]
        
    def test_sum(self):
        # data = [1,2,3,4]
        self.assertEqual(sum(self.data), 10, 'should be 10')
    
    def test_sum_tuple(self):
        self.assertEqual(sum(self.data), 9)
    


if __name__ == '__main__':
    unittest.main()
    print('Everything passed')