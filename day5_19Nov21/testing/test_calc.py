### All tests start with name test_*

import unittest

import calc

class TestCalc(unittest.TestCase): # Test suite! 
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, 0), -1)
        self.assertEqual(calc.add(-1, -1), -2)
    
    def test_divide(self):
        self.assertEqual(calc.divide(6, 2), 3)
        self.assertEqual(calc.divide(-1, 1), -1)

        with self.assertRaises(ValueError):
            calc.divide(3, 0)

if __name__ == '__main__':
    unittest.main()