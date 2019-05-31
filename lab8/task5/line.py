from point import *


class Line:
    """
    class for representing line using two dots
    """

    def __init__(self, a, b):
        """
        initialisation of the class
        :param a: first point
        :param b: second point
        """
        self.a = a
        self.b = b

    def __str__(self):
        """
        method for representing Line in string
        :return: needed str
        """
        return "[{}, {}], [{}, {}]".format(self.a.x,
                                           self.a.y,
                                           self.b.x,
                                           self.b.y)

    def __repr__(self):
        """
        method for representing Line in string
        :return: needed str
        """
        return "Line <Point[{}, {}], Point[{}, {}]>".format(self.a.x,
                                                            self.a.y,
                                                            self.b.x,
                                                            self.b.y)

    def intersect(self, other):
        """
        method for checking if two lines intersect or not
        :param other: other Line instance
        :return: the self element if lines are equal, None if they are
        parallel, Point of intersect otherwise
        """
        k1, b1 = self.line_equation()
        k2, b2 = other.line_equation()
        if b1 is None and b2 is None:
            if k1 == k2:
                return self
            else:
                return None
        elif b1 is None:
            x = k1
            y = k2 * k1 + b2
            return Point(x, y)
        elif b2 is None:
            x = k2
            y = k2 * k1 + b1
            return Point(x, y)
        else:
            x = (b2 - b1) / (k1 - k2)
            y = (k1 * b2 - b1 * k2) / (k1 - k2)
            return Point(x, y)

    def line_equation(self):
        """
        Method for searching coefficients of the line equation
        :return: needed coeffs
        """
        try:
            k = (self.b.y - self.a.y) / (self.b.x - self.a.x)
            b = self.a.y - self.a.x * (self.b.y - self.a.y) / (
                    self.b.x - self.a.x)
        except ZeroDivisionError:
            return self.a.x, None
        return k, b
