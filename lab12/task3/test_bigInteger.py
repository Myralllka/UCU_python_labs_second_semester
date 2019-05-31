from unittest import TestCase
from bigintager import BigInteger


class TestBigInteger(TestCase):
    def setUp(self):
        self.a = BigInteger('123')
        self.b = BigInteger('-22987')
        self.c = BigInteger('123')
        self.d = BigInteger('1241')
        self.e = BigInteger('-1233')
        self.w = BigInteger('-1000')
        self.big = BigInteger('999')
        self.small = BigInteger('9')
        self.aa = BigInteger('20')
        self.lst = [BigInteger('123'),
                    BigInteger('-22987'),
                    BigInteger('123'),
                    BigInteger('1241'),
                    BigInteger('-1233'),
                    BigInteger('-1000'),
                    BigInteger('999'),
                    BigInteger('9'),
                    BigInteger('0'),
                    BigInteger('9999999999999'),
                    BigInteger('-1000000')]

    def test1(self):
        def test_eq(self):
            self.assertEqual(self.a, self.c)
            self.assertNotEqual(self.a, self.b)

        def test_repr(self):
            self.assertEqual(repr(self.a), '123')

        def test_len(self):
            self.assertEqual(len(self.b), 5)
            self.assertEqual(len(self.a), 3)

        def test_gt(self):
            self.assertGreater(self.a, self.b)
            self.assertGreater(self.e, self.b)
            self.assertGreater(self.w, self.e)

        def test_ge(self):
            self.assertGreaterEqual(self.d, self.c)
            self.assertGreaterEqual(self.a, self.c)
            self.assertGreaterEqual(self.w, self.e)

        def test_lt(self):
            self.assertLess(self.c, self.d)
            self.assertLess(self.b, self.e)
            self.assertLess(self.e, self.d)
            self.assertLess(self.e, self.w)

        def test_le(self):
            self.assertLessEqual(self.c, self.a)
            self.assertLessEqual(self.e, self.d)
            self.assertLessEqual(self.e, self.w)

        def test_ne(self):
            self.assertNotEqual(self.a, self.b)
            self.assertNotEqual(self.a, self.d)
            self.assertNotEqual(self.w, self.e)

        test_eq(self)
        test_repr(self)
        test_len(self)
        test_gt(self)
        test_ge(self)
        test_lt(self)
        test_len(self)
        test_le(self)
        test_ne(self)

    # def test2(self):
    def test_add(self):
        for i in self.lst:
            for j in self.lst:
                self.assertEqual(str(i + j),
                                     str(int(str(i)) + int(str(j))))

    def test_sub(self):
        for i in self.lst:
            for j in self.lst:
                self.assertEqual(str(i - j),
                                 str(int(str(i)) - int(str(j))))

    def test_mul(self):
        for i in self.lst:
            for j in self.lst:
                # try:
                self.assertEqual(str(i * j),
                                 str(int(str(i)) * int(str(j))))
                # except AssertionError:
                #     print(i, j)

    def test_div(self):
        for i in self.lst:
            for j in range(-200, 200):
                if j == 0:
                    continue
                self.assertEqual(str(i // j),
                                 str(int(str(i)) // int(str(j))))

    def test_mod(self):
        for i in self.lst:
            for j in range(-200, 200):
                if j == 0:
                    continue
                self.assertEqual(str(i % j),
                                 str(int(str(i)) % int(str(j))))

    # def test_pow(self):
