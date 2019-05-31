import classroom


class AcademicBuilding:
    """
    class for representing of academic building with classes
    """

    def __init__(self, address, classrooms):
        """
        Initialize of AcademicBuilding class

        :param address: str - address of the building
        :param classrooms: list - list of classrooms in this building

        """
        self.classrooms = classrooms
        self.address = address

    def __str__(self):
        """
        Print class information for NONProgramers
        :return:
        """
        return "{}\n{}".format(self.address, "\n".join(str(i) for i in
                                                       self.classrooms))

    def total_equipment(self):
        """
        Take total information about equipment in the building

        :return: list - list of tuples of pares: equipment end the number
        of it
        """
        result = []
        for each in self.classrooms:
            result.extend(each.equipment)
        result.sort()
        result = set((i, result.count(i)) for i in result)
        result = sorted(list(result))
        return result
