#!/bin/env ipython

from zip_processor import *
from scale_zip import *
from zip_replace import *
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        fname = input('print here file name of the archive: ')
    else:
        fname = sys.argv[1]
    tmp = input('if there is text in your archive, print "1", if images - '
                '"2": ')
    if tmp == '1':
        ZipProcessor(fname, ZipReplace())
    elif tmp == '2':
        ZipProcessor(fname, ScaleZip())
    else:
        print('incorrect input')
