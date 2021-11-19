### All tests start with name test_*

import unittest

import calc

class TestCalc(unittest.TestCase): # Test suite! 
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, 0), -1)
        self.assertEqual(calc.add(-1, -1), -2)
    
if __name__ == '__main__':
    unittest.main()