# Implementation of the Polynomial ADT using a sorted linked list.


class Polynomial:
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    def __repr__(self):
        current = self._poly_head
        res = ''
        while current is not None:
            if current.coefficient == 0:
                continue
            elif current.coefficient == 1:
                res += 'x^{:.0f} + '.format(current.degree)
            elif current.degree == 0:
                res += '{:.0f}+ '.format(current.coefficient)
            elif current.degree == 1:
                res += '{:.0f}x + '.format(current.coefficient)
            else:
                res += '{:.0f}x^{:.0f} + '.format(current.coefficient,
                                                  current.degree)
            current = current.next
        return res[:-2]

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree >= degree:
            cur_node = cur_node.next
        if cur_node is None or cur_node.degree != degree:
            return 0.0
        else:
            return cur_node.coefficient

    # Polynomial addition: new_poly = self + rhs_poly.
    def __add__(self, rhs_poly):
        assert self.degree() >= 0 and rhs_poly.degree() >= 0, "Addition only " \
                                                              "allowed on non -empty polynomials."
        new_poly = Polynomial()
        node_a = self._poly_head
        node_b = rhs_poly._poly_head

        # Add corresponding terms until one list is empty.
        while node_a is not None and node_b is not None:
            if node_a.degree > node_b.degree:
                degree = node_a.degree
                value = node_a.coefficient
                node_a = node_a.next
            elif node_a.degree < node_b.degree:
                degree = node_b.degree
                value = node_b.coefficient
                node_b = node_b.next
            else:
                degree = node_a.degree
                value = node_a.coefficient + node_b.coefficient
                node_a = node_a.next
                node_b = node_b.next
            new_poly._append_term(degree, value)

        # If self list contains more terms append them.
        while node_a is not None:
            new_poly._append_term(node_a.degree, node_a.coefficient)
            node_a = node_a.next

        # Or if rhs contains more terms append them.
        while node_b is not None:
            new_poly._append_term(node_b.degree, node_b.coefficient)
            node_b = node_b.next

        return new_poly

    # Polynomial subtraction: new_poly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        assert self.degree() >= 0 and rhs_poly.degree() >= 0, "Addition only " \
                                                              "allowed on non -empty polynomials."
        new_poly = Polynomial()
        node_a = self._poly_head
        node_b = rhs_poly._poly_head

        # Add corresponding terms until one list is empty.
        while node_a is not None and node_b is not None:
            if node_a.degree > node_b.degree:
                degree = node_a.degree
                value = node_a.coefficient
                node_a = node_a.next
            elif node_a.degree < node_b.degree:
                degree = node_b.degree
                value = -node_b.coefficient
                node_b = node_b.next
            else:
                degree = node_a.degree
                value = node_a.coefficient - node_b.coefficient
                node_a = node_a.next
                node_b = node_b.next
            new_poly._append_term(degree, value)

        # If self list contains more terms append them.
        while node_a is not None:
            new_poly._append_term(node_a.degree, node_a.coefficient)
            node_a = node_a.next

        # Or if rhs contains more terms append them.
        while node_b is not None:
            new_poly._append_term(node_b.degree, node_b.coefficient)
            node_b = node_b.next

        return new_poly

    # Polynomial multiplication: new_poly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        if type(rhs_poly) == Polynomial:
            assert self.degree() >= 0 and rhs_poly.degree() >= 0, "Addition only " \
                                                                  "allowed on non -empty polynomials."
            if rhs_poly._poly_head.next is None:
                new_poly = Polynomial()
                node_a = self._poly_head
                while node_a is not None:
                    new_poly._append_term(
                            rhs_poly._poly_head.degree + node_a.degree,
                            rhs_poly._poly_head.coefficient * node_a.coefficient)
                    node_a = node_a.next
                return new_poly
            else:
                node_a = self
                node_b = rhs_poly._poly_head
                new_poly = node_a * Polynomial(
                        degree=node_b.degree, coefficient=node_b.coefficient)
                node_b = node_b.next
                while node_b is not None:
                    new_poly += node_a * Polynomial(
                            degree=node_b.degree,
                            coefficient=node_b.coefficient)
                    node_b = node_b.next
                return new_poly
        elif type(rhs_poly) == int:
            return Polynomial(
                    degree=self.degree(),
                    coefficient=(self._poly_head.coefficient * rhs_poly))

            # Helper method for appending terms to the polynomial.

    def _append_term(self, degree, coefficient):
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None:
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Return the degree of the polynomial.
    def degree(self):
        if self._poly_head is None:
            return -1
        else:
            return self._poly_head.degree


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
