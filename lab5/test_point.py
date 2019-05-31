#!/bin/env python3

from point import Point
import doctest

points = [Point(1, 1), Point(3, 1), Point(2, 3), Point(1, 1)]
print(points[0])
print(repr(points[0] == points[2]))
print(repr(points[0] == points[3]))
