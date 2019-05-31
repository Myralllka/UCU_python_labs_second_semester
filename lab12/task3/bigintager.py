from node import *
import re


class BigInteger:
    def __init__(self, value):
        assert value != '', 'value must not be empty string'
        if len(value) > 1 and int(value) == 0:
            value = '0'

        self.head = TwoWayNode(value[0], None, None)
        head = self.head
        tail = None
        for each in value[1:]:
            head.next = TwoWayNode(each, head, tail)
            head = head.next
        self.tail = head

    def __repr__(self):
        head = self.head
        res = ''
        checker = False
        while head is not None:
            res += str(head.data)
            if head.data not in '-0':
                checker = True
            head = head.next
        if checker:
            return res
        return '0'

    def __len__(self):
        head = self.head
        if self.head.data == '-':
            head = self.head.next
        counter = 0
        while head is not None:
            counter += 1
            head = head.next
        return counter

    def __eq__(self, other):
        if isinstance(other, int):
            other = BigInteger(str(other))
        if len(self) != len(other):
            return False
        head1, head2 = self.head, other.head
        while head1 is not None:
            if head1.data != head2.data:
                return False
            head1, head2 = head1.next, head2.next
        return True

    def __gt__(self, other):
        if isinstance(other, int):
            other = BigInteger(str(other))
        if self == other:
            return False
        if self.head.data != '-' and other.head.data == '-':
            return True
        if self.head.data == '-' and other.head.data != '-':
            return False
        head1, head2, negative = self.head, other.head, False
        if head1.data == '-':
            head1, head2 = head1.next, head2.next
            negative = True
        if len(self) < len(other):
            return negative
        elif len(self) > len(other):
            return not negative
        while head1 is not None:
            if (head1.data > head2.data and negative or
                    head1.data < head2.data and not negative):
                return False
            if head1.data > head2.data and not negative:
                return True
            head1, head2 = head1.next, head2.next
        return True

    def __lt__(self, other):
        if isinstance(other, int):
            other = BigInteger(str(other))
        return not (self > other or self == other)

    def __ge__(self, other):
        return self > other or self == other

    def __pos__(self):
        res = BigInteger(str(self))
        if res.head.data == '-':
            res.head = res.head.next
            res.head.previous = None
        return res

    def __neg__(self):
        res = BigInteger(str(self))
        if res.head.data == '-':
            return + res
        res.head = TwoWayNode('-', None, res.head)
        return res

    def __add__(self, other):
        if isinstance(other, int):
            other = BigInteger(str(other))
        if self.head.data == '-' and other.head.data == '-':
            return - (+ self + (+ other))
        elif self.head.data == '-':
            return -(+ self - other)
        elif other.head.data == '-':
            return self - (+other)
        maxx = self.max_one(other)
        minn = self.min_one(other)
        tail1, tail2 = maxx.tail, minn.tail
        while tail2 is not None:
            tail1.data = str(int(tail1.data) + int(tail2.data))
            tail1, tail2 = tail1.previous, tail2.previous
        tail1 = maxx.tail
        while tail1 is not None:
            if int(tail1.data) > 9:
                if tail1.previous is not None:
                    tail1.previous.data = str(int(tail1.previous.data) + 1)
                else:
                    maxx.head = TwoWayNode(str(int(tail1.data) // 10), None,
                                           maxx.head)
                tail1.data = str(int(tail1.data) - 10)
            tail1 = tail1.previous
        while maxx.head.data == '0' and maxx.head.next is not None:
            maxx.head = maxx.head.next
            maxx.head.previous = None
        return maxx

    def __sub__(self, other):
        if isinstance(other, int):
            other = BigInteger(str(other))
        if self.head.data == '-' and other.head.data == '-':
            return - (+ self - (+ other))
        elif self.head.data == '-':
            return - (+self + other)
        elif other.head.data == '-':
            return self + (+other)
        maxx = self.max_one(other)
        minn = self.min_one(other)
        tail1, tail2 = maxx.tail, minn.tail
        while tail2 is not None:
            tail1.data = str(int(tail1.data) - int(tail2.data))
            tail1, tail2 = tail1.previous, tail2.previous
        tail1 = maxx.tail
        while tail1.previous is not None:
            if int(tail1.data) < 0:
                tail1.previous.data = str(int(tail1.previous.data) - 1)
                tail1.data = str(int(tail1.data) + 10)
            tail1 = tail1.previous
        while maxx.head.data == '0' and maxx.head.next is not None:
            maxx.head = maxx.head.next
            maxx.head.previous = None
        if self == minn:
            return - maxx
        return maxx

    def __mul__(self, other):
        if isinstance(other, int):
            other = BigInteger(str(other))
        if self == BigInteger('1'):
            return other.copy()
        if other == BigInteger('1'):
            return self.copy()
        if str(other) in re.findall(r'10+', str(other)):
            return BigInteger(str(self) + '0' * (len(other) - 1))
        sign = False
        if self.head.data == '-' or other.head.data == '-':
            sign = True
        if self.head.data == '-' and other.head.data == '-':
            sign = False
        maxx = (+ self).max_one((+ other))
        minn = (+ self).min_one((+ other))
        tail2, res = minn.tail, BigInteger('0')
        i = BigInteger('1')
        while tail2 is not None:
            tail1 = maxx.tail
            counter = BigInteger('1') * i
            while tail1 is not None:
                res += (BigInteger(str(int(tail1.data) * int(
                        tail2.data))) * counter)
                counter.tail.next = TwoWayNode('0', counter.tail, None)
                counter.tail = counter.tail.next
                tail1 = tail1.previous
            i.tail.next = TwoWayNode('0', counter.tail, None)
            i.tail = i.tail.next
            tail2 = tail2.previous
        if sign:
            return - res
        return res

    def __floordiv__(self, other):
        n1 = self.copy()
        if other == 0:
            raise ZeroDivisionError
        elif other == 1:
            return n1
        if self.head.data == '-':
            if str((+ self) % other) == '0':
                return -((+self) // other)
            return -((+self) // other + 1)
        elif other < 0:
            if str(self % (-other)) == '0':
                return -(self // (-other))
            else:
                return -((self // (-other)) + 1)
        if n1 < other:
            return 0
        head1 = n1.head
        tmp = head1.data
        res = ''
        while head1.next is not None:
            while (int(tmp) / other < 1) and (int(tmp) / other != .0) \
                    and head1 is not None:
                head1 = head1.next
                res += '0'
                if head1 is None:
                    while res[0] == '0':
                        res = res[1:]
                    return BigInteger(res)
                tmp += head1.data
            head1 = head1.next
            res += str(int(tmp) // other)
            if head1 is None:
                while res[0] == '0':
                    res = res[1:]
                return BigInteger(res)
            tmp = str(int(tmp) % other) + head1.data
        res += str(int(tmp) // other)
        while res[0] == '0':
            res = res[1:]
        return BigInteger(res)

    def __mod__(self, other):
        b = self - ((self // other) * other)
        return b

    def __pow__(self, power, modulo=None):
        tmp = self.copy()
        for _ in range(power - 1):
            tmp *= self
        return tmp

    def to_bin(self):
        res = ''
        current = self.copy()
        while str(current) != '1':
            res = str(current % 2) + res
            current //= 2
        res = str(current) + res
        return res

    @staticmethod
    def to_int(number):
        res = BigInteger('0')
        mul = BigInteger('1')
        for element in number[::-1]:
            res += mul * int(element)
            mul *= 2
        return res

    def __lshift__(self, other):
        return self.to_int(self.to_bin() + '0' * other)

    def __rshift__(self, other):
        return self.to_int(self.to_bin()[:-other])

    def __and__(self, other):
        a1, a2 = self.to_bin()[::-1], other.to_bin()[::-1]
        tmp1, tmp2, i = a1[0], a2[0], 0
        res = ''
        while True:
            res += str(int(tmp1) and int(tmp2))
            i += 1
            try:
                tmp1, tmp2 = a1[i], a2[i]
            except:
                break
        return self.to_int(res[::-1])

    def __or__(self, other):
        a1, a2 = self.to_bin()[::-1], other.to_bin()[::-1]
        while len(a1) != len(a2):
            if len(a1) > len(a2):
                a2 += '0'
            else:
                a1 += '0'
        tmp1, tmp2, i = a1[0], a2[0], 0
        res = ''
        while True:
            res += str(int(tmp1) or int(tmp2))
            i += 1
            try:
                tmp1, tmp2 = a1[i], a2[i]
            except:
                break
        return self.to_int(res[::-1])

    def __xor__(self, other):
        a1, a2 = self.to_bin()[::-1], other.to_bin()[::-1]
        while len(a1) != len(a2):
            if len(a1) > len(a2):
                a2 += '0'
            else:
                a1 += '0'
        tmp1, tmp2, i = a1[0], a2[0], 0
        res = ''
        while True:
            if tmp1 == tmp2:
                res += '0'
            else:
                res += '1'
            i += 1
            try:
                tmp1, tmp2 = a1[i], a2[i]
            except:
                break

        return self.to_int(res[::-1])

    def max_one(self, other):
        """
        return copy of the max element
        """
        if self == other:
            return other.copy()
        if self > other:
            return self.copy()
        else:
            return other.copy()

    def min_one(self, other):
        """
        return copy of the min element
        """
        if self == other:
            return other.copy()
        if self > other:
            return other.copy()
        else:
            return self.copy()

    def copy(self):
        """
        :return: copy of the element
        """
        return BigInteger(str(self))
