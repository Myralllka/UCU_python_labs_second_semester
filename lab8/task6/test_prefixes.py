from unittest import TestCase
from all_prefix import *
import unittest


class TestAll_prefixes(TestCase):
    def setUp(self):
        self.n1 = ''
        self.n2 = ''
        self.n3 = ''
        self.n4 = ''

    def test_all_prefixes_1(self):
        self.assertEqual(all_prefixes('avangard'),
                         {'angar', 'ar', 'ang', 'avan', 'angard', 'avangar',
                          'an', 'a', 'avanga', 'anga', 'av', 'ard', 'avang',
                          'ava', 'avangard'})

    def test_all_prefixes_2(self):
        self.assertEqual(all_prefixes('lead'), {"l", "le", "lea", "lead"})

    def test_all_prefixes_3(self):
        self.assertEqual(all_prefixes('bumblebee'),
                         {'bumble', 'blebee', 'bee', 'bumbl', 'bumb', 'b',
                          'ble', 'bumblebee', 'bleb', 'bl', 'bum', 'blebe',
                          'be', 'bumbleb', 'bu', 'bumblebe'})

    def test_all_prefixes_4(self):
        self.assertEqual(all_prefixes('assertequal'),
                         {'a', 'al', 'assertequal', 'asserte', 'asserteq',
                          'assertequa', 'ass', 'asser', 'as', 'assertequ',
                          'assert', 'asse'})


if __name__ == '__main__':
    unittest.main()
