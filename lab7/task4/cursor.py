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
        self.position will be incremented and you still can insert the
        symbols but if you try to delete the symbol on the current position -
        you will have IndexError. And the same if you try to move to home
        or end.
        """
        self.position += 1

    def back(self):
        """
        Method for moving the cursor back on one position. if you move the
        cursor to position before zero and try to insert something,
        the characters will be inserted on the '-1', '-2' positions, to the
        end of the file, but you still can move to the home and to the end
        """
        self.position -= 1

    def home(self):
        """
        Method for moving cursor on the start of the current line
        """
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before new line
                break

    def end(self):
        """
        Method for moving cursor on the end of the current line
        :return:
        """
        while (self.position < len(self.document.characters) and
               self.document.characters[self.position].character != '\n'):
            self.position += 1
