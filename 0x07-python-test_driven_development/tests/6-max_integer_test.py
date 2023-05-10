#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test max_integer with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test max_integer with a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-5, 0, 10, -2]), 10)

    def test_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers"""
        self.assertEqual(max_integer([1, 2, 2, 3, 3, 3]), 3)

    def test_large_numbers(self):
        """Test max_integer with a list of large numbers"""
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)

if __name__ == '__main__':
    unittest.main()

