from unittest import TestCase
from is_sorted import *
import unittest


class TestIs_sorted(TestCase):
    def test_is_sorted_1(self):
        self.assertEqual(is_sorted([]), True)

    def test_is_sorted_2(self):
        self.assertEqual(is_sorted([0, 1, 2, 2, 2, 3, 100, 10000]), True)

    def test_is_sorted_3(self):
        self.assertEqual(is_sorted([1, 1, 0]), False)

    def test_is_sorted_4(self):
        self.assertEqual(is_sorted([1, 2, 3, 4, 6, 7, 89, 8]), False)


if __name__ == '__main__':
    unittest.main()
