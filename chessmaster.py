#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: The Chess Piece"""

import time


class ChessPiece(object):
    """chess piece class"""

    prefix = ""
    moves = []

    def __init__(self, position):
        self.position = position
        if not self.is_on_board(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """convert position to ordered pair and vice versa"""

        conversion_dict = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }
        x = conversion_dict.get(tile[0])
        y = int(tile[1]) - 1
        position = (x, y)
        if x is None or y > 7:
            position = None

        return position

    def is_legal_move(self, position):
        """is move legal"""

        return self.algebraic_to_numeric(position) is not None

    def move(self, position):
        """move chesspiece"""

        if self.is_legal_move(position):

            current_move = (
                self.prefix + self.position,
                self.prefix + position,
                time.time()
            )
            moves.append(current_move)
            self.position = position
            return current_move

        else:
            return False

    def is_on_board(self, position):
        """is piece on board"""

        numeric = self.algebraic_to_numeric(position)
        return True if numeric is not None else False

class Rook(ChessPiece):
    """rook chesspiece"""

    def __init__(self):
        super(ChessPiece, self).__init__()
        self.prefix = "R"
    def is_legal_move(self, position):
        if super


class Bishop(ChessPiece):
    """bishop chesspiece"""

    def __init__(self):
        super(ChessPiece, self).__init__()
        self.prefix = "B"

class King(ChessPiece):
    """king chesspiece"""

    def __init__(self):
        super(ChessPiece, self).__init__()
        self.prefix = "K"





class ChessMatch(object):
    """game board and track match"""

    def __init__(self, pieces=None):
        if pieces:
            self.reset(pieces)




if __name__ == "__main__":
    cp = ChessPiece('a9')