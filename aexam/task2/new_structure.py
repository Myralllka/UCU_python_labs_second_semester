import random
from node import *


class Struct:
    """
    Structure of random int elements based on linked nodes
    """
    RANGE = 10  # range of random numbers (from zero to RANGE including RANGE)

    def __init__(self, n):
        """
        initialization of class instance
        :param n: number of random numbers
        """
        self.head = Node(random.randint(0, Struct.RANGE))
        self.point = self.head
        for i in range(n):
            random_number = random.randint(0, Struct.RANGE)
            self.point.next = Node(random_number)
            self.point = self.point.next

    def __str__(self):
        res = ''
        point = self.head
        while point.next is not None:
            res += '{} -> '.format(point.data)
            point = point.next
        return res + 'null'

    def remove_duplicates(self):
        """
        method for removing all duplicates element in structure
        """
        point = self.head.next
        point_prev = self.head
        includes = set()
        includes.add(point_prev.data)
        while point.next is not None:
            if point.data in includes:
                point = point.next
                point_prev.next = point
                continue
            else:
                includes.add(point.data)
            point_prev = point
            point = point.next

# s = Struct(15)
# print(s)
# s.remove_duplicates()
# print(s)
