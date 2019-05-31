"""
File: testbst.py

A tester program for binary search trees.
"""

from linkedbst import LinkedBST
import random


def main():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nExpect True for A in tree: ", "A" in tree)

    print("\nString:\n" + str(tree))

    clone = LinkedBST(tree)
    print("\nClone:\n" + str(clone))

    print("Expect True for tree == clone: ", tree == clone)

    print("\nFor loop: ", end="")
    for item in tree:
        print(item, end=" ")

    print("\n\nin_order traversal: ", end="")
    for item in tree.in_order():
        print(item, end=" ")

    # print("\n\npreorder traversal: ", end="")
    # for item in tree.pre_order(): print(item, end = " ")

    # print("\n\npostorder traversal: ", end="")
    # for item in tree.post_order(): print(item, end = " ")

    # print("\n\nlevelorder traversal: ", end="")
    # for item in tree.level_order(): print(item, end = " ")

    print("\n\nRemoving all items:", end=" ")
    for item in "ABCDEFG":
        print(tree.remove(item), end=" ")

    print("\n\nExpect 0: ", len(tree))

    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))

    lyst = list(range(1, 16))

    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))

    lyst = [113, 30, 68, 74, 45, 91, 88]
    # random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print(tree, tree.height())
    print(tree.is_balanced())
    print(tree.range_find(30, 91))
    print(tree.successor(113))
    print(tree.predecessor(113))
    tree.rebalance()
    print(tree)


# print("\nAdded ", lyst, "\n" + str(tree))
# tree.remove(10)
# print("\nAdded ", lyst, "\n" + str(tree))
# tree.remove(12)
# print("\nAdded ", lyst, "\n" + str(tree))


if __name__ == "__main__":
    # main()
    # lyst = [30, 68, 74, 45, 91, 88, 111, 4, 5, 6, 7, 11, 8, 1, 2, 3]
    lyst = [30, 68, 74, 45, 91, 88, 111, 1, 2, 6, 7, 3, 4, 10, 8, 5]
    # lyst = [i for i in range(10)]
    # lyst = [2, 1, 3, 4, 0]
    # lyst = [1, 2, 3, 4]
    # random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print(tree)
    print(tree.is_balanced())
    print(tree.height())
    print('-'*10)
    tree.rebalance()
    print(tree)
    # print()
    # print(tree.is_balanced())
    # print([i for i in tree.range_find(10, 100)])
