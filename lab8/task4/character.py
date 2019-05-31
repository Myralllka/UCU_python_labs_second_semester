from exceptions import *


class Character:
    """
    class for representing characters in the document

    """

    def __init__(self,
                 character: str,
                 bold=False,
                 italic=False,
                 underline=False):
        """
        initialization of the character instance
        if len of character is not 1, user will get TooMuchCharacters
        :param character:  current character
        :param bold: True if the character is bold, False if not
        :param italic: True if character is italic, False if not
        :param underline: True if character is underlined, False if not
        """
        if len(character) != 1:
            raise TooMuchCharacters
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        Method for representing the character in the right way
        :return: str - needed string
        """
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character
