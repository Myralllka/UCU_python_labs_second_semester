from binary_search_tree.linkedbst import LinkedBST
import time
import random


def read_file(filename):
    res = set()
    with open(filename, 'r', encoding='utf-8') as ff:
        for line in ff.readlines():
            res.add(line.strip())
    return res


def main():
    tmp_set, tmp_list = read_file('words.txt'), []
    searching_list = []
    counter = 0
    while True:
        try:
            tmp_list.append(tmp_set.pop())
            counter += 1
        except KeyError:
            break
    tmp_set = read_file('words.txt')
    counter = 0
    while counter < 10000:
        counter += 1
        searching_list.append(tmp_set.pop())
    tree = LinkedBST(tmp_list)
    print(
            'a) визначити час пошуку 10000 випадкових слів у впорядкованому за абеткою словнику (пошук у списку слів з використанням методів вбудованого типу list).')
    time1 = time.time()
    for word in searching_list:
        l1 = tmp_list.index(word)
    print(time.time() - time1)

    print(
            'b) визначити час пошуку 10000 випадкових слів у словнику, який представлений у вигляді бінарного дерева пошуку. Бінарне дерево пошуку будується на основі словника в якому слова не впорядковані за абеткою. ')
    time1 = time.time()
    for word in searching_list:
        tree.find(word)
    print(time.time() - time1)
    
    if not tree.is_balanced():
        tree.rebalance()

    print(
            'c) Визначити час пошуку 10000 випадкових слів у словнику, який представлений у вигляді збалансованого бінарного дерева пошуку.')

    time1 = time.time()
    for word in searching_list:
        tree.find(word)
    print(time.time() - time1)
    # print(tree)


main()
# print(read_file('words.txt'))
