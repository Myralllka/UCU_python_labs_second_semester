class Classroom:
    """
    class for representation classrooms
    """

    def __init__(self, number, capacity, equipment):
        """
        Initialize of Classroom class

        :param number: str - classroom number
        :param capacity: int - count of workspaces in the classroom
        :param equipment: list - material support for classes that teachers
        can use
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """
        Print class information for NONProgramers

        :return: str - message for users that contain information about the
        classroom
        """
        return """Classroom {} has a capacity of {} persons and has the \
following equipment: {}.""".format(self.number, self.capacity,
                                   ", ".join(self.equipment))

    def __repr__(self):
        """
        Print class information for programmers

        :return: str - message for users that contain information about the
        classroom
        """
        class_name = type(self).__name__
        return "{}('{}', {}, ['{}'])".format(class_name, self.number,
                                             self.capacity,
                                             "', '".join(self.equipment))

    def is_larger(self, other_self):
        """
        Compare classrooms by capacity

        :param other_self: class instance - other classroom
        :return: bool - True if first classroom can contain more people,
        False if not
        """
        return self.capacity > other_self.capacity

    def equipment_differences(self, other_self):
        """
        Compare classrooms equipment

        :param other_self: class instance - other classroom
        :return: list - elements that exist in first class instance and does
        not in the other
        """
        return [i for i in self.equipment if i not in other_self.equipment]
