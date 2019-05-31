"""
File: linkedbst.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from math import log


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, source_collection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a pre_order traversal on a view of self."""
        if not self.is_empty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.is_empty():
                node = stack.pop()
                yield node.data
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)

    def pre_order(self):
        """Supports a pre_order traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node is not None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def in_order(self):
        """Supports an in_order traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def post_order(self):
        """Supports a post_order traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)

        recurse(self._root)
        return iter(lyst)

    def level_order(self):
        """Supports a level_order traversal on a view of self."""
        return

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) is not None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left is None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right is None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.is_empty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        post condition: item is removed from self."""
        if item not in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def lift_max_in_left_subtree_to_top(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            current_node = top.left
            while current_node.right is not None:
                parent = current_node
                current_node = current_node.right
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else:
                parent.right = current_node.left

        # Begin main part of the method
        if self.is_empty():
            return None

        # Attempt to locate the node containing the item
        item_removed = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        direction = 'L'
        current_node = self._root
        while current_node is not None:
            if current_node.data == item:
                item_removed = current_node.data
                break
            parent = current_node
            if current_node.data > item:
                direction = 'L'
                current_node = current_node.left
            else:
                direction = 'R'
                current_node = current_node.right

        # Return None if the item is absent
        if item_removed is None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the max node in the left subtree
        if current_node.left is not None \
                and not current_node.right is None:
            lift_max_in_left_subtree_to_top(current_node)
        else:

            # Case 2: The node has no left child
            if current_node.left is None:
                new_child = current_node.right

                # Case 3: The node has no right child
            else:
                new_child = current_node.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = new_child
            else:
                parent.right = new_child
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.is_empty():
            self._root = None
        else:
            self._root = pre_root.left
        return item_removed

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe is not None:
            if probe.data == item:
                old_data = probe.data
                probe.data = new_item
                return old_data
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self) -> int:
        """
        Return the height of tree
        """

        def tmp(p):
            """
            helping function
            :param p: current
            :return:
            """
            if p is None:
                return 0
            else:
                return max(tmp(p.left) + 1, tmp(p.right) + 1)

        return tmp(self._root)

    def is_balanced(self) -> bool:
        """
        Return True if tree is balanced
        """
        # print(self.height(),  2 * log(self._size + 1, 2) - 1)
        return self.height() < 1.44 * log(self._size, 2) - 1

    def rebalance(self):
        """
        Re balances the tree.
        :return: rebalanced tree
        """

        def tmp(qq, lst):
            tmp_lst = [lst]
            while True:
                new_tmp_lst = []
                for l in tmp_lst:
                    if not l:
                        tmp_lst.remove(l)
                        continue
                    qq.add(l[len(l) // 2])
                    new_tmp_lst.append(l[:len(l) // 2])
                    new_tmp_lst.append(l[len(l) // 2 + 1:])
                if not tmp_lst:
                    break
                tmp_lst = new_tmp_lst
            res = [i for i in qq]
            return res

        res = [i for i in self.in_order()]
        q = LinkedQueue()
        tmp_list = (tmp(q, res))
        self.clear()
        for each in tmp_list:
            self.add(each)

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item: comparable element
        :return: None if there is no item in the tree, otherwise searched item
        """
        tmp = [i for i in self.in_order()]
        for i in range(self._size):
            if tmp[i] == item:
                try:
                    return tmp[i + 1]
                except IndexError:
                    return None
        return None

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :return:
        """
        tmp = [i for i in self.in_order()]
        for i in range(self._size):
            if tmp[i] == item:
                try:
                    return tmp[i - 1]
                except IndexError:
                    return None
        return None

    def range_find(self, low, high):
        """
        Returns a list of the items in the tree, where low <= item <= high.
        :param low: lowest element
        :param high: highest element
        :return: list of elements between lowest and highest
        """
        return [i for i in self if low < i < high]
