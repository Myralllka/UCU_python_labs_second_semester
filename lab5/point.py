class Point:
    """
    Representing Point on the Cartesian coordinate system
    """

    def __init__(self, x=0, y=0):
        """
        Initialize the position of a new point. The x and y coordinates can
        be specified. If they are not, the point defaults to the origin.

        :param x: float - coordinate by x
        :param y: float - coordinate by Y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Print class information for NONProgramers

        :return: str - message for users that contain information about the
        point
        """
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        """
        Compare tuo dots for their coordinates

        :param other: point instance
        :return: bool - True if points have same coordinates, False if not
        """
        return self.x == other.x and self.y == other.y
