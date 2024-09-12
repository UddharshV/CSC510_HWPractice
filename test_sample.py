"""
Module contains the unit test case for the exponent calculation
"""
import unittest
from myfile import recursive_expo


class TestMyFile(unittest.TestCase):
    """
    Test cases for recursive exponent calculation
    """

    def test_case1(self):
        """
        2^3=8
        """
        self.assertEqual(recursive_expo(2,3), 8)
    def test_case2(self):
        """
        2^4=16
        """
        self.assertEqual(recursive_expo(2,4), 16)

if __name__ == '__main__':
    unittest.main()