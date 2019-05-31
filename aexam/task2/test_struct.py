import copy
from unittest import TestCase
from new_structure import *
import random


class TestStruct(TestCase):

    def setUp(self) -> None:
        random.seed(1)
        self.s1 = Struct(10)
        self.s2 = Struct(5)
        self.s3 = Struct(50)
        print(self.s1)

    def test_remove_duplicates_1(self):
        new = copy.copy(self.s1)
        new.remove_duplicates()
        sett = set()
        new_set = set()
        point = self.s1.head
        while point.next is not None:
            sett.add(point.data)
            point = point.next

        point = new.head
        while point.next is not None:
            new_set.add(point.data)
            point = point.next
        self.assertEqual(sett, new_set)


    def test_remove_duplicates_2(self):
        new = copy.copy(self.s3)
        new.remove_duplicates()
        sett = set()
        new_set = set()
        point = self.s3.head
        while point.next is not None:
            sett.add(point.data)
            point = point.next

        point = new.head
        while point.next is not None:
            new_set.add(point.data)
            point = point.next
        self.assertEqual(sett, new_set)

    def test_remove_duplicates_str(self):
        self.assertEqual(str(self.s1),
                         '2 -> 9 -> 1 -> 4 -> 1 -> 7 -> 7 -> 7 -> 10 -> 6 -> null')
