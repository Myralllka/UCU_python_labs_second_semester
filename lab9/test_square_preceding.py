from unittest import TestCase
from square_preceding import *
import coverage


class TestSquare_preceding(TestCase):
    def test_1(self):
        self.lst = []
        square_preceding(self.lst)
        self.assertEqual([], self.lst, 'error with empty list')

    def test_2(self):
        self.lst = [-2, -5]
        square_preceding(self.lst)
        self.assertEqual([0, 4], self.lst, 'error with negative elements')

    def test_3(self):
        self.lst = [2]
        square_preceding(self.lst)
        self.assertEqual([0], self.lst, 'error with one element')

    def test_4(self):
        self.lst = [2, 3, 4, 5, 6, 7, 8, 9]
        square_preceding(self.lst)
        self.assertEqual([0, 4, 9, 16, 25, 36, 49, 64], self.lst, 'error '
                                                                  'with a lot of elements')
