class Polynomial:
    """
    class for representing polynomials
    """

    def __init__(self, coeffs: list):
        """
        initialisation of object of this class
        :param coeffs: list of coeffs of current polynomial
        """
        self.coeffs = []
        tmp = [0] if coeffs == [] else coeffs
        flag = False
        if len(tmp) >= 1:
            for each in tmp:
                if each != 0:
                    flag = True
                if flag:
                    self.coeffs.append(each)

    def __str__(self):
        """
        return string representing of the polynomial
        :return: needed string
        """
        return 'Polynomial(coeffs={})'.format(self.coeffs)

    def __eq__(self, other):
        """
        check if two instances of class are equal or not
        """
        if len(self.coeffs) == 1:
            if self.coeffs[0] == other:
                return True
            return False
        elif not isinstance(other, Polynomial):
            return False
        elif len(self.coeffs) != len(other.coeffs):
            return False
        else:
            for i in range(len(self.coeffs)):
                if self[i] != other[i]:
                    return False
        return True

    def __getitem__(self, item: int) -> int:
        """
        it helps to get items from polynomial, to write instead of
        self.coeffs[i] just self[i]
        :param item: index of needed coeff
        :return: index`s coeff
        """
        return self.coeffs[item]

    def __hash__(self):
        """
        method to hash polynomials
        :return:
        """
        return hash(tuple(self.coeffs))

    def degree(self) -> int:
        """
        method for checking max degree of polynomial
        :return:
        """
        return len(self.coeffs) - 1

    def coeff(self, number: int) -> int:
        """
        returns the coefficient for x**i
        :param number: coeff
        :return: coefficient for x**i
        """
        return self[::-1][number]

    def evalAt(self, x: int) -> int:
        """
        count the result of polynomial in 'x'
        :param x: needed x position
        :return:
        """
        tmp = self[::-1]
        result = tmp[0]
        for i in range(1, len(tmp)):
            result += x ** i * (tmp[i])
        return result

    def scaled(self, x: int):
        """
        scale the polynomial in x times
        :return: new polynomial with scaled coeffs
        """
        return self.__class__(list(map(lambda i: i * x, self.coeffs)))

    def derivative(self):
        """
        will return a new polynomial that is the derivative of the original
        :return: new polynomial - derivative of original
        """
        tmp, result = self[::-1], []
        for i in range(1, len(tmp)):
            result.append(tmp[i] * i)
        return self.__class__(result[::-1])

    def addPolynomial(self, other):
        """
        add the coefficients of any terms with the same degree, and return a
        new polynomial
        :param other: other polynomial
        :return: new polynomial with new coeffs
        """
        if not isinstance(other, Polynomial):
            return None
        tmp_list1 = self[::-1]
        tmp_list2 = other[::-1]
        l1, l2 = sorted([tmp_list1, tmp_list2])[1], sorted([tmp_list1,
                                                            tmp_list2])[0]
        i = 0
        for each in l2:
            l1[i] += each
            i += 1
        return self.__class__(l1[::-1])

    def multiplyPolynomial(self, other):
        """
        multiply the coefficients of two polynomials and return a new
        polynomial with the correct coefficients.
        :param other: other polynomial instance
        :return: new polynomial with multiplied coeffs
        """
        tmp1 = self[::-1]
        tmp2 = other[::-1]
        result = [0] * (len(tmp1) + len(tmp2) - 1)
        for i in range(len(tmp1)):
            for j in range(len(tmp2)):
                result[i + j] += tmp1[i] * tmp2[j]
        return self.__class__(result[::-1])


class Quadratic(Polynomial):
    """
    class for representing quadratic polynomial
    We use the quadratic formula to find the function's roots.
    """

    def __init__(self, coeffs):
        """
        initialisation of class`s object.
        :param coeffs: list of coeffs of current polynomial
        """
        assert len(coeffs) == 3
        super().__init__(coeffs)

    def __str__(self):
        """
        return string representing of the polynomial
        :return: needed string
        """
        return 'Quadratic(a={}, b={}, c={})'.format(self[0], self[1], self[2])

    def discriminant(self) -> int:
        """
        the discriminant is b**2 - 4ac
        :return: int - needed discriminant
        """
        return self[1] ** 2 - 4 * self[0] * self[2]

    def numberOfRealRoots(self) -> int:
        """
        search number of roots of the quadratic
        :return: number of roots
        """
        if self.discriminant() < 0:
            return 0
        elif self.discriminant() == 0:
            return 1
        else:
            return 2

    def getRealRoots(self) -> list:
        """
        search roots of the quadratic
        :return: list of roots or empty one, depends on number of real roots
        """
        d = self.discriminant() ** .5
        if self.numberOfRealRoots() == 2:
            p1 = (self[1] * (-1) + d) / 2 * self[0]
            p2 = (self[1] * (-1) - d) / 2 * self[0]
            return sorted([p1, p2])
        elif self.numberOfRealRoots() == 1:
            return [(self[1] * (-1) - d) / 2 * self[0]]
        else:
            return []
