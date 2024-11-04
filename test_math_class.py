import unittest
from math_class import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(1,-1), 0)
        self.assertEqual(add(-1000, -2000), -3000)
        self.assertEqual(add("one", "two"), TypeError)

if __name__ == '__main__':
    unittest.main() 