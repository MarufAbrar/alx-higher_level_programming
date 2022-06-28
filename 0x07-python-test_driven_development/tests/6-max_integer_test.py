#!/usr/bin/python3
"""Unittests for max_integer
"""

import unittest
import random


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit test for the max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1,2,3,7,4,5,6]), 7)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 1.7, 2.8]), 2.8)

    def test_string_implicit_ansii_values(self):
        self.assertEqual(max_integer('abcd'), 'd')

    def test_empty_string(self):
        self.assertEqual(max_integer(''), None)


if __name__ == '__main__':
    unittest.main()
