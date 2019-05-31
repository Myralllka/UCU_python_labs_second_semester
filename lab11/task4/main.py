#!/bin/env python

# this module based on this one https://github.com/b9nc9/python-lzw

from GrayscaleImg import *
import random
import re


img = GrayscaleImg(40, 20)
for i in range(img.height()):
    for j in range(img.width()):
        img[i, j] = random.choice([i for i in range(30)])


def compress(image):
    """
    function for compressing image
    :param image: current image
    :return: compressed image
    """
    compressed = ""
    compress_dictionary = dict()
    for i in range(0, 256):
        compress_dictionary[chr(i)] = str(i)
    a = ""
    for b in image:
        key = a + b
        if key in compress_dictionary:
            a = key
        else:
            compressed += str(compress_dictionary[a]) + " "
            compress_dictionary[key] = len(compress_dictionary)
            a = b
    if a != "":
        compressed += str(compress_dictionary[a])
    return compressed


def decompress(compressed):
    """
    function for decompression compressed image
    :param compressed: compressed image
    :return: decompressed image
    """
    decompress_dictionary = dict()
    l = list(map(int, compressed.split(' ')))
    for i in range(0, 256):
        decompress_dictionary[i] = chr(i)
    a = str(decompress_dictionary[l[0]])
    decompressed = a
    l.pop(0)
    for i in l:
        entry = ""
        if i in decompress_dictionary:
            entry = decompress_dictionary[i]
        elif i == len(decompress_dictionary):
            entry = a + a[0]
        decompressed += entry
        decompress_dictionary[len(decompress_dictionary)] = a + entry[0]
        a = entry
    res = GrayscaleImg(decompressed.find('\n') // 3,
                       len(decompressed.split('\n')))
    t, tmp = [(re.findall('...', i)) for i in decompressed.split('\n')], []
    for each in t:
        tmp.extend(each)
    tmp, counter = [int(i) for i in tmp], 0

    for i in range(res.height()):
        for j in range(res.width()):
            res[i, j] = tmp[counter]
            counter += 1
    return res


tmp = compress(str(img))
print('original:')
print(img)
print('after compressing: ')
print(tmp)
print('after decompressing:')
print(decompress(tmp))
