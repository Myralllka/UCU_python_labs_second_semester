from document import *


if __name__ == '__main__':
    """
    code for checking if the program works or not
    """
    d = Document()
    for c in 'Hello, my friend,\nyou are grate':
        d.insert(c)
    print(d.string)
    print(d.cursor.position)
    d.cursor.forward()
    print(d.cursor.position)
    for i in range(3):
        d.cursor.forward()
    print(d.cursor.position)
    print(d.string)
    d.insert('!')
    print(d.cursor.position)
    print(d.string)
    try:
        d.delete()
    except IndexError as e:
        print(e.args)
    try:
        d.cursor.home()
    except IndexError as e:
        print(e.args)
    for i in range(5):
        d.cursor.back()
    d.delete()
    print(d.cursor.position)
    print(d.string)
    d.cursor.home()
    print(d.cursor.position)
    print(d.string)
    d.cursor.back()
    d.cursor.home()
    print(d.cursor.position)
    d.cursor.back()
    print(d.cursor.position)
    d.insert('?')
    print(d.string)
    d.cursor.home()
    print(d.cursor.position)
    d.cursor.end()
    print(d.cursor.position)
    d.cursor.forward()
    d.cursor.end()
    print(d.cursor.position)
    try:
        d.delete()
    except IndexError as e:
        print(e.args)
    try:
        d.save()
    except FileNotFoundError as e:
        print(e.args)
    try:
        d.insert('sss')
    except AssertionError as e:
        print('Assertion error')
