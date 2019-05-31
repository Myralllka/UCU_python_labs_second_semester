from multiset.node import *

# A class implementing Multiset as a linked list.


class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def __str__(self):
        current = self._head
        res = ''
        while current is not None:
            res += str(current.item) + '\n'
            current = current.next
        return res

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def remove_all(self):
        """
        Remove all nodes
        :return: list with nodes items
        """
        lst = []
        current = self._head
        while current is not None:
            lst.append(current.item)
            current = current.next
        self._head = None
        return lst

    def copy(self):
        """
        :return: copy of the class instance
        """
        tmp = Multiset()
        head = self._head
        while head is not None:
            tmp.add(head)
            head = head.next
        res = Multiset()
        head = tmp._head
        while head is not None:
            res.add(head)
            head = head.next
        return res

    def __reversed__(self):
        tmp = Multiset()
        head = self._head
        while head is not None:
            tmp.add(head)
            head = head.next
        return tmp

    def split_half(self):
        """
        Split structure by two half
        :return: two Multiset - first and second half of the input Multiset
        """
        if self._head.next is None:
            return (None, None)
        head, tmp = self._head, self._head
        even = 0
        part1 = Multiset()
        part2 = Multiset()
        while head is not None:
            even += 1
            if even % 2 == 0:
                part1.add(tmp)
                tmp = tmp.next
            head = head.next
        while tmp is not None:
            part2.add(tmp)
            tmp = tmp.next
        return part1.__reversed__(), part2.__reversed__()

    def add(self, value):
        """
        Adds the value to multiset.
        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """
        Delete the value from multiset
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
