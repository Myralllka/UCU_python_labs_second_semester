#!/bin/env python3

from point import Point
from triangle import Triangle
import doctest


triangle = Triangle(Point(1,1), Point(3,1), Point(2,3))
print(repr(triangle.is_triangle()))
print(repr(triangle.perimeter()))
print(repr(triangle.area()))
triangle = Triangle(Point(1, 1), Point(1, 1), Point(2, 2))
print(repr(triangle.perimeter()))
print(repr(triangle.area()))
