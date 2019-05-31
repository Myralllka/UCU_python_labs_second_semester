from modules import *

pieces = {
    'empty': Empty(),
    'w_rook': Rook('w'),
    'b_rook': Rook('b'),
    'r_rook': Rook('r'),
    'y_rook': Rook('y'),
    'w_bishop': Bishop('w'),
    'b_bishop': Bishop('b'),
    'r_bishop': Bishop('r'),
    'y_bishop': Bishop('y'),
    'w_knight': Knight('w'),
    'b_knight': Knight('b'),
    'r_knight': Knight('r'),
    'y_knight': Knight('y'),
    'w_king': King('w'),
    'b_king': King('b'),
    'r_king': King('r'),
    'y_king': King('y'),
    'w_queen': Queen('w'),
    'b_queen': Queen('b'),
    'r_queen': Queen('r'),
    'y_queen': Queen('y'),
    'w_pawn': Pawn('w'),
    'b_pawn': Pawn('b'),
    'r_pawn': Pawn('r'),
    'y_pawn': Pawn('y')
    }

l = [
    ChessSet(GlinskiBoard(pieces)),
    ChessSet(StandardBoard(pieces)),
    ChessSet(FourBoard(pieces)),
    ChessSet(DoubleBoard(pieces)),
    ChessSet(ThreeBoard(pieces))
    ]
for each in l:
    print(each, '\n\n')
