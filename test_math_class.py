import unittest
from math_class_arithmetic import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    """
    A test class for the `add` function in the `math_class` module.

    This class contains unit tests to verify the correct behavior of the `add` function for various input values.
    """
    def test_add(self):
        """
        Tests the `add` function with different input values.

        This test method covers the following scenarios:
        - Adding two positive integers.
        - Adding a positive and a negative integer.
        - Adding two negative integers.
        - Adding two non-numeric strings (expected to raise a TypeError).
        """
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(1,-1), 0)
        self.assertEqual(add(.15,.17), .32)
        self.assertEqual(add(-1000, -2000), -3000)
        self.assertEqual(add("one", "two"), TypeError)

    def test_subtract(self):
        """
        Tests the `subtract` function with different input values.

        This test method covers the following scenarios:
        - Subracting two positive integers.
        - Subracting two positive integers to equal 0.
        - Subtracting two float decimals.
        - Subtracting two negative integers.
        - Subtracting two non-numeric strings (expected to raise a TypeError).
        """
        self.assertEqual(subtract(2,3), -1)
        self.assertEqual(subtract(1,1), 0)
        self.assertEqual(subtract(.50,.25), .25)
        self.assertEqual(subtract(-1000, -2000), 1000)
        self.assertEqual(subtract("one", "two"), TypeError)

    def test_multiply(self):
        """
        Tests the `multilply` function with different input values.

        This test method covers the following scenarios:
        - Multiplying two positive integers.
        - Multiplying two positive integers to equal 0.
        - Multiplying two float decimals.
        - Multiplying two negative integers.
        - Multiplying two non-numeric strings (expected to raise a TypeError).
        """
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(1,1), 1)
        self.assertEqual(multiply(.50,.25), .125)
        self.assertEqual(multiply(-1000, -2000), 2000000)
        self.assertEqual(multiply("one", "two"), TypeError)        

if __name__ == '__main__':
    unittest.main() 