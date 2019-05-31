import copy


class Board:
    """
    class for representing chess board
    """
    def __init__(self, pieces: dict):
        """
        initialization of chess board class for different boards
        :param pieces: dictionary of Pieces instances
        """
        self.pieces = pieces

    def __str__(self):
        """
        Method to print information about the class
        :return: string, also a chess board
        """
        return '\n'.join([str(i) for i in self.board]) \
            .replace(', ', ' ')

    def __repr__(self):
        """
        Method for representation information about the Board
        :return: same as __str__ method
        """
        return self.__str__()

    def set_positions(self):
        """
        function to set position of the pieces on the board. All boards have
        their own start set and positions for all pieces
        :return:
        """
        pass


class StandardBoard(Board):
    """
    class for representation standard 8*8 chess board
    (https://en.wikipedia.org/wiki/Chessboard)
    """
    def __init__(self, pieces):
        super().__init__(pieces)
        self.board = [[self.pieces['empty'] for i in range(8)] for j in
                      range(8)]
        self.set_positions()

    def set_positions(self):
        for i in range(8):
            self.board[1][i] = self.pieces['w_pawn']
            self.board[6][i] = self.pieces['b_pawn']
            if i == 0 or i == 7:
                self.board[0][i] = self.pieces['w_rook']
                self.board[7][i] = self.pieces['b_rook']
            elif i == 1 or i == 6:
                self.board[0][i] = self.pieces['w_knight']
                self.board[7][i] = self.pieces['b_knight']
            elif i == 2 or i == 5:
                self.board[0][i] = self.pieces['w_bishop']
                self.board[7][i] = self.pieces['b_bishop']
        self.board[0][3] = self.pieces['w_queen']
        self.board[7][3] = self.pieces['b_king']
        self.board[0][4] = self.pieces['w_king']
        self.board[7][4] = self.pieces['b_queen']


class DoubleBoard(StandardBoard):
    """
    class for representing 12*16 chess board. it looks same as standard
    board, but more free space between pieces and number of figures is
    doubled (https://uk.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Double_Chess_gameboard_and_init_config.png)
    """
    def __init__(self, pieces):
        super().__init__(pieces)
        for i in range(4):
            self.board.insert(3, [self.pieces['empty'] for i in range(8)])
        for row in self.board:
            tmp = copy.deepcopy(row)
            row.extend(tmp)


class ThreeBoard(Board):
    """
    class for representation of Board for three players
    (https://uk.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Chess_for_Three_-_Hexagonal_Board.jpg)
    """
    def __init__(self, pieces):
        super().__init__(pieces)
        self.board = [[None for i in range(12)] for j in range(12)]
        for i in range(12):
            for j in range(12):
                if i < 4 and j > 7:
                    continue
                if i > 7 and j < 4:
                    continue
                if 3 < i < 8 and 3 < j < 8:
                    continue
                self.board[i][j] = self.pieces['empty']
        self.set_positions()

    def __str__(self):
        new_line = ''
        letters = 'abcdefghijkl'
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j] is None:
                    new_line += str(self.board[i][j]) + '({},{})' \
                        .format(letters[j], i + 1)

            new_line += '\n'
        return new_line

    def set_positions(self):
        for i in range(12):  # i - letters
            if i < 8:
                self.board[1][i] = self.pieces['w_pawn']
            if i < 4 or i > 7:
                self.board[6][i] = self.pieces['r_pawn']
            if i >= 4:
                self.board[10][i] = self.pieces['b_pawn']
        self.board[0][0] = self.pieces['w_rook']
        self.board[0][7] = self.pieces['w_rook']
        self.board[0][1] = self.pieces['w_king']
        self.board[0][6] = self.pieces['w_king']
        self.board[0][2] = self.pieces['w_bishop']
        self.board[0][5] = self.pieces['w_bishop']
        self.board[7][0] = self.pieces['r_rook']
        self.board[7][11] = self.pieces['r_rook']
        self.board[7][1] = self.pieces['r_king']
        self.board[7][10] = self.pieces['r_king']
        self.board[7][2] = self.pieces['r_bishop']
        self.board[7][9] = self.pieces['r_bishop']
        self.board[11][7] = self.pieces['b_rook']
        self.board[11][11] = self.pieces['b_rook']
        self.board[11][6] = self.pieces['b_knight']
        self.board[11][10] = self.pieces['b_knight']
        self.board[11][5] = self.pieces['b_bishop']
        self.board[11][9] = self.pieces['b_bishop']
        self.board[11][8] = self.pieces['b_king']
        self.board[11][4] = self.pieces['b_queen']
        self.board[7][8] = self.pieces['r_queen']
        self.board[7][3] = self.pieces['r_king']
        self.board[0][3] = self.pieces['w_queen']
        self.board[0][4] = self.pieces['w_king']


class GlinskiBoard(Board):
    """
    class for representing Glinski chess board
    (https://uk.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Glinski_Chess_Setup.png)
    """
    def __init__(self, pieces):
        super().__init__(pieces)
        self.board = [[None for i in range(11)] for j in range(11)]
        for i in range(11):
            for j in range(11):
                if i + j > 4 and j - i < 6:
                    self.board[i][j] = self.pieces['empty']
        self.set_positions()

    def __str__(self):
        new_line = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j] is None:
                    new_line += str(self.board[i][j])
                else:
                    new_line += ' '*4

            new_line += '\n'
        return new_line

    def set_positions(self):
        for i in range(1, 10):
            self.board[4][i] = self.pieces['b_pawn']
        for i in range(3):
            self.board[i][5] = self.pieces['b_bishop']
            self.board[i + 8][5] = self.pieces['w_bishop']
        for i in range(10, 4, -1):
            for j in range(1, 11):
                if i + j == 11 and j < 6:
                    self.board[i][j] = self.pieces['w_pawn']
        for i in range(4):
            self.board[i+7][i+6] = self.pieces['w_pawn']
        self.board[10][2] = self.pieces['w_rook']
        self.board[10][8] = self.pieces['w_rook']
        self.board[10][3] = self.pieces['w_knight']
        self.board[10][7] = self.pieces['w_knight']
        self.board[10][6] = self.pieces['w_king']
        self.board[10][4] = self.pieces['w_queen']
        self.board[3][2] = self.pieces['b_rook']
        self.board[3][8] = self.pieces['b_rook']
        self.board[2][3] = self.pieces['b_knight']
        self.board[2][7] = self.pieces['b_knight']
        self.board[1][6] = self.pieces['b_king']
        self.board[1][4] = self.pieces['b_queen']


class FourBoard(Board):
    """
    class for representing of Board for chess for four players
    (https://uk.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Four-handed_chess.png)
    """
    def __init__(self, pieces):
        super().__init__(pieces)
        self.board = [[self.pieces['empty'] for i in range(14)] for j in range(
                14)]
        for i in range(14):
            for j in range(14):
                if (i < 3 and j < 3 or
                        i < 3 and j > 10 or
                        i > 10 and j < 3 or
                        i > 10 and j > 10):
                    self.board[i][j] = None
        self.set_positions()

    def set_positions(self):
        for i in range(3, 11):
            self.board[1][i] = self.pieces['b_pawn']
            self.board[12][i] = self.pieces['w_pawn']
            self.board[i][1] = self.pieces['y_pawn']
            self.board[i][12] = self.pieces['r_pawn']
            if i == 3 or i == 10:
                self.board[0][i] = self.pieces['b_rook']
                self.board[13][i] = self.pieces['w_rook']
                self.board[i][0] = self.pieces['y_rook']
                self.board[i][13] = self.pieces['r_rook']
            if i == 4 or i == 9:
                self.board[0][i] = self.pieces['b_knight']
                self.board[13][i] = self.pieces['w_knight']
                self.board[i][0] = self.pieces['y_knight']
                self.board[i][13] = self.pieces['r_knight']
            if i == 5 or i == 8:
                self.board[0][i] = self.pieces['b_bishop']
                self.board[13][i] = self.pieces['w_bishop']
                self.board[i][0] = self.pieces['y_bishop']
                self.board[i][13] = self.pieces['r_bishop']
            self.board[0][6] = self.pieces['b_king']
            self.board[13][7] = self.pieces['w_king']
            self.board[6][0] = self.pieces['y_king']
            self.board[7][13] = self.pieces['r_king']
            self.board[0][7] = self.pieces['b_queen']
            self.board[13][6] = self.pieces['w_queen']
            self.board[7][0] = self.pieces['y_queen']
            self.board[6][13] = self.pieces['r_queen']
