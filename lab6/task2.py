class Furniture:
    """
    Class for representing furniture objects
    """
    def __init__(self, style, assign):
        """

        :param style: str
        :param assign: str
        """
        self.style = style
        self.assign = assign

    def __str__(self, ch=''):
        return "<{}furniture style is {}>".format(ch, self.style)

    def __eq__(self, other):
        """

        :param other: class instance
        :return:
        """
        return self.style == other.style and self.assign == other.assign

    def get_assign(self):
        """
        return instance assign
        """
        return self.assign


class Chair(Furniture):
    """
    class for representing chair objects
    """
    def __init__(self, style, assign, tipe):
        """

        :param style: str
        :param assign: str
        :param tipe: str
        """
        super().__init__(style, assign)
        self.tipe = tipe

    def __str__(self):
        return '{}'.format(super().__str__(ch='This armchair '))


if __name__ == '__main__':

    furniture1 = Furniture("empire", "bedroom")

    furniture2 = Furniture("modern", "bathroom")

    assert (not (furniture1 == furniture2))

    assert (furniture1.style == "empire")

    assert (furniture1.assign == "bedroom")

    assert (str(furniture1) == "<furniture style is empire>")

    chair1 = Chair("empire", "bedroom", "armchair")

    assert (chair1.tipe == "armchair")

    assert (isinstance(chair1, Furniture))

    assert (str(chair1) == "<This armchair furniture style is empire>")

    assert (chair1.get_assign() == "bedroom")
