from unittest import TestCase
from line import *


class TestLine(TestCase):
    def setUp(self):
        self.A = Point(-1, -1)
        self.B = Point(2, 5)
        self.C = Point(0, 4)
        self.D = Point(1, 2)
        self.E = Point(2, 3)
        self.F = Point(2, -1)
        self.X = Point(2, -3)
        self.Y = Point(2, -4)
        self.M = Point(-2, -5)
        self.N = Point(2, -5)
        self.L = Point(1, 0)
        self.m = Line(self.D, self.L)
        self.a = Line(self.A, self.B)
        self.b = Line(self.C, self.D)
        self.c = Line(self.E, self.F)
        self.d = Line(self.X, self.Y)
        self.k = Line(self.M, self.N)

    def test_same(self):
        self.assertEqual(self.c.intersect(self.d), self.c)

    def test_parallel(self):
        self.assertIsNone(self.c.intersect(self.m))

    def test_1(self):
        self.assertEqual(self.a.intersect(self.d), Point(2, 5))

    def test_2(self):
        self.assertEqual(self.d.intersect(self.k), Point(2, -5))

    def test_3(self):
        self.assertEqual(self.a.intersect(self.b), Point(0.75, 2.5))

    def test_print_repr(self):
        self.assertEqual(str(self.a), '[-1.0, -1.0], [2.0, 5.0]')
        self.assertEqual(str(self.B), '[2.0, 5.0]')
        self.assertEqual(repr(self.k), 'Line <Point[-2.0, -5.0], '
                                       'Point[2.0, -5.0]>')
        self.assertEqual(repr(self.X), 'Point[2.0, -3.0]')
