from Stack.linkedstack import *


class Palindrome:
    def __init__(self):
        self.en, self.ua = self.read_from_file('words.txt'), \
                           self.read_from_file('base.lst')
        self.words_processing()
        self.write_to_file('palindrome_en.txt', self.en)
        self.write_to_file('palindrome_uk.txt', self.ua)

    @staticmethod
    def read_from_file(filename):
        res = []
        with open(filename, 'r', encoding='utf-8') as file:
            for word in file:
                res.append(word.split()[0].strip())
        return res

    @staticmethod
    def write_to_file(filename, items):
        with open(filename, 'w') as file:
            for word in items:
                print(word, file=file)

    @staticmethod
    def check_the_word(word):
        tmp = LinkedStack()
        for letter in word[:len(word) // 2]:
            tmp.push(letter)
        for letter in word[len(word) // 2 + len(word) % 2:]:
            item = tmp.pop()
            if letter != item:
                return False
        return True

    def find_palindromes(self, lst):
        res = []
        for word in lst:
            if self.check_the_word(word):
                res.append(word)
        return res

    def words_processing(self):
        self.en = self.find_palindromes(self.en)
        self.ua = self.find_palindromes(self.ua)


a = Palindrome()
# a = LinkedStack()
# lw = 'abccba'
# for i in lw[:len(lw)//2]:
#     a.push(i)
# for i in lw[len(lw) // 2 + len(lw) % 2:]:
#     item = a.pop()
#     print(i, item)


# print(a)
# print(a.pop())
# print(a)
# print(lw[:len(lw)//2])
# print(lw[len(lw) // 2 + len(lw) % 2:])