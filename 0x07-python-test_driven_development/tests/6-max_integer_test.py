#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        This class is for testing max_integer function
        by unittest module
    """
    def test_normal_values(self):
        """
        test_normal_values(self) - tests normal values
        param self: self object parameter
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 10, 13, 50]), 50)

    def test_empty_list(self):
        """
        test_empty_list(self) - tests empty list
        param self: self object parameter
        """
        self.assertFalse(max_integer(list()))

    def test_same_values(self):
        """
        test_same_values(self) - tests a list with the same values
        param self: self object parameter
        """
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

    def test_all_zeros(self):
        """
        test_all_zeros(self) - tests a list with all zeros
        param self: self object parameter
        """
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

    def test_only_one(self):
        """
        test_only_one(self) - tests a list with only one element
        param self: self object parameter
        """
        self.assertEqual(max_integer([0]), 0)

    def test_many_values(self):
        """
        test_many_values(self) - tests a list values from -1000 to 1000
        param self: self object parameter
        """
        self.assertEqual(max_integer(list(range(-1000, 1001))), 1000)

    def test_negative_values1(self):
        """
        test_negative_values(self) - tests a list with negative values
        param self: self object parameter
        """
        self.assertEqual(max_integer([-999999999] +
                                     list(range(-1000, 1001))), 1000)

    def test_negative_values2(self):
        """
        test_negative_values(self) - tests a list with negative values
        param self: self object parameter
        """
        self.assertEqual(max_integer(list(range(-1000, -60))), -61)

    def test_large_positive_values(self):
        """
        test_large_positive_values(self) - tests with large positive values
        param self: self object parameter
        """
        self.assertEqual(max_integer(list(range(100000,
                                                500001))), 500000)

    def test_weird_mix(self):
        """
        test_weird_mix(self) - tests with positive, negative, and large values
        param self: self object parameter
        """
        self.assertEqual(max_integer([1, 3, 324432, 923840, 100000, 23840,
                                     444, 1000, -34, -60, 133, 1000,
                                     343, 44, 23, 3434, 2423, 2, 423, 10, 100,
                                     43, 23, 900, 78, 465, -10000,
                                     490]), 923840)

    def test_list_of_strings(self):
        """
        This tests whether the function gives correct
        output for list of strings or not
        """
        self.assertEqual(max_integer(["Belal", "Youssef",
                                     "Doaa", "Aya"]), "Youssef")


if __name__ == '__main__':
    unittest.main()
