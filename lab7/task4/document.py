from cursor import *
from character import *


class Document:
    """
    class for representing document with characters and cursor
    """
    def __init__(self):
        """
        initialization of the document object
        characters - list of character instances on the document
        cursor - cursor instance
        filename - name of the current file
        """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        Method for insert character on the needed position. If you will try
        to insert more than one character in one cell, you will get an
        AssertionError
        :param character: character instance that you insert
        """
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        Method for delete the character instance from current cursor position
        If you will try to delete the symbol after the last position,
        you will get the IndexError.
        """
        del self.characters[self.cursor.position]

    def save(self):
        """
        Method for saving the current document with it`s filename.
        If you will try to save the file without the input name, you will
        get the FileNotFoundError.
        """
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        """
        Method for displaying the document inside text in normal representation
        :return: str, needed string
        """
        return ''.join(str(i) for i in self.characters)
