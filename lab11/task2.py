class MarsType:
    """
    class for representing type for Mars task
    """

    def __init__(self, symbol, start=0):
        self._start = start
        self._symbol = str(symbol)
        self._items = self.convert()

    def __getitem__(self, item):
        return self._items[item]

    def __repr__(self):
        return '{}'.format(self._items)

    def convert(self):
        """
        method for converting symbol into needed format
        :return:
        """
        def checker(element):
            if element > 180:
                element -= 360
            return element
        tmp = hex(ord(self._symbol))[2:]
        tmp1, tmp2 = int(tmp[0], 16), int(tmp[1], 16)
        tmp1 = tmp1 * 22.5 - self._start
        tmp1 = checker(tmp1)
        tmp2 = tmp2 * 22.5 - tmp1 - self._start
        tmp2 = checker(tmp2)
        finish = tmp2 + tmp1 + self._start
        return tuple([tmp1, tmp2, finish])


class MarsCoder:
    """
    class for representing codes for Mars type
    """
    def __init__(self, text):
        """
        initialization of the class
        :param text: text to code or decode
        """
        self._text = text
        self._items = self.decode()

    def __repr__(self):
        return '{}'.format(self._items)

    def decode(self):
        """
        method for decoding the text
        :return: list of angles
        """
        tmp, result = list(), list()
        tmp.append(MarsType(self._text[0]))
        for i in range(1, len(self._text)):
            index = tmp[i-1][2]
            tmp.append(MarsType(self._text[i], index))
        for i in tmp:
            result.extend([(i[0]), (i[1])])
        return result


a = MarsCoder('Hello')
print(a)
