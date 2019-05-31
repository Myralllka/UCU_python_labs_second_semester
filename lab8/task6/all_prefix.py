#!/bin/env python3


def all_prefixes(string: str) -> set:
    """
    function to search all prefixes - parts of the word
    that starts from the first letter of the word
    """
    tmp = string[::-1]
    first = string[0]
    result = set()
    number_of_iters = len(tmp)
    number_of_first = tmp.count(first)
    for num in range(number_of_first):
        for i in range(number_of_iters):
            result.add(tmp[::-1])
            tmp = tmp[1:]
        tmp = string[string[1:].find(first) + 1:][::-1]
        number_of_iters = len(tmp)
        string = tmp[::-1]
    return result


# print(all_prefixes('assertequal'))
