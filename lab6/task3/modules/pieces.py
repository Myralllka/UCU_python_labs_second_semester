class Piece:
    """
    class for representation chess pieces
    """

    def __init__(self, color: str):
        """
        initialization of Piece class
        :param color:
        """
        self.color = color

    def __repr__(self):
        """
        Method for representation the information about Piece
        :return: piece shape and it`s color
        """
        if self.color is None:
            return ' (e)'
        return '{}({})'.format(self.shape, self.color)

    def move(self):
        """
        Method for chess piece movement
        """
        pass


class Empty(Piece):
    def __init__(self):
        super().__init__(None)
        self.shape = ' '


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.shape = chr(9814)

    def move(self):
        pass


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.shape = chr(9815)

    def move(self):
        pass


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.shape = chr(9816)

    def move(self):
        pass


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.shape = chr(9812)

    def move(self):
        pass


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.shape = chr(9813)

    def move(self):
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.shape = chr(9817)

    def move(self):
        pass
