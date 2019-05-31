class Triangle:
    """
    Representing Triangle using points on the Cartesian coordinate system
    """

    def __init__(self, vertex1, vertex2, vertex3):
        """
        Initialize the triangle by their vertexes

        :param vertex1: point instance
        :param vertex2: point instance
        :param vertex3: point instance
        """
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

    @staticmethod
    def to_edge(ver1, ver2):
        """
        Staticmethod to convert to points into edge

        :param ver1: point instance
        :param ver2: point instance
        :return: float - length of the edge
        """
        return ((ver2.x - ver1.x) ** 2 + (ver2.y - ver1.y) ** 2) ** .5

    def is_triangle(self):
        """
        Check if figure is triangle or not
        :return: bool - True if figure is triangle, else False
        """
        if (self.vertex1 == self.vertex2 or
                self.vertex2 == self.vertex3 or
                self.vertex1 == self.vertex3):
            return False
        edges = sorted([Triangle.to_edge(self.vertex1, self.vertex2),
                        Triangle.to_edge(self.vertex1, self.vertex3),
                        Triangle.to_edge(self.vertex3, self.vertex2)])
        if sum(edges[1:]) > edges[0]:
            return True
        return False

    def perimeter(self):
        """
        Calculate the perimeter of the triangle

        :return: float - triangle perimeter
        """
        if self.is_triangle():
            return sum([Triangle.to_edge(self.vertex1, self.vertex2),
                        Triangle.to_edge(self.vertex1, self.vertex3),
                        Triangle.to_edge(self.vertex3, self.vertex2)])
        return 'Not a triangle'

    def area(self):
        """
        Calculate the value of area of the triangle

        :return: float - triangle value of area
        """
        if not self.is_triangle():
            return 'Not a triangle'
        a, b, c, p = [Triangle.to_edge(self.vertex1, self.vertex2),
                      Triangle.to_edge(self.vertex1, self.vertex3),
                      Triangle.to_edge(self.vertex3, self.vertex2),
                      self.perimeter() / 2]
        return (p * (p - a) * (p - b) * (p - c)) ** .5
