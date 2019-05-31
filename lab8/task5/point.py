class Point:
    """
    class for representing the point
    """

    def __init__(self, x: float, y: float):
        """
        initialisation of the class
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """
        method for representing Line in string
        :return: needed str
        """
        return '[{}, {}]'.format(self.x, self.y)

    def __repr__(self):
        """
        method for representing Line in string
        :return: needed str
        """
        return 'Point[{}, {}]'.format(self.x, self.y)

    def __eq__(self, other):
        """
        method for checking if two instances are equal or not
        :param other:
        :return:
        """
        return self.x == other.x and self.y == other.y
