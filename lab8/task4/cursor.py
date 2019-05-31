from exceptions import *


class Cursor:
    """
    class for representing cursor in the document
    """

    def __init__(self, document):
        """
        initialization of the cursor instance
        :param document: document instance
        """
        self.document = document
        self.position = 0

    def forward(self):
        """
        Method for moving the cursor forward on one position
        If you continue to move cursor forward the last symbol,
        you will have OutOfDocument.
        """
        if self.position < 0 or self.position >= len(
                self.document.characters) + 1:
            raise OutOfDocument('You can`t move after the end!')
        self.position += 1

    def back(self):
        """
        Method for moving the cursor back on one position. if you try to
        move the cursor to position before zero and try to insert something,
        you will get the OutOfDocument exception

        """
        if self.position <= 1 or self.position > len(
                self.document.characters) + 1:
            raise OutOfDocument('You can`t move before the start!')
        self.position -= 1

    def home(self):
        """
        Method for moving cursor on the start of the current line
        """

        if self.position <= 1 or self.position >= len(
                self.document.characters):
            raise OutOfDocument('You can`t move before the start!')
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before new line
                break

    def end(self):
        """
        Method for moving cursor on the end of the current line
        """
        if self.position <= 1 or self.position >= len(
                self.document.characters):
            raise OutOfDocument('You can`t move after the end!')
        while (self.position < len(self.document.characters) and
               self.document.characters[self.position].character != '\n'):
            self.position += 1
