#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: The Chess Piece"""

import time


class ChessPiece(object):
    """chess piece class"""

    prefix = ''
    moves = []

    def __init__(self, position):

        if not ChessPiece.is_legal_move(self, position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

        self.position = position


    def algebraic_to_numeric(self, tile):
        """convert position to ordered pair and vice versa"""

        coordinate = list(tile)
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
        x = conversion_dict.get(coordinate[0])
        y = int(coordinate[1]) - 1
        position = (x, y)
        if x is None or y > 7:
            position = None

        print position
        return position

    def is_legal_move(self, position):
        """is move legal"""
        numeric = self.algebraic_to_numeric(position)
        # return self.algebraic_to_numeric(position) is not None
        return True if numeric is not None else False

    def move(self, position):
        """move chesspiece"""

        if self.is_legal_move(position):

            current_move = (
                self.prefix + self.position,
                self.prefix + position, time.time()
            )
            self.moves.append(current_move)
            self.position = position
            return current_move

        else:
            return False


class Rook(ChessPiece):
    """rook chesspiece"""

    prefix = 'R'

    def is_legal_move(self, position):
        """
         :param position:
         :return:
         """

        newpos = self.algebraic_to_numeric(position)
        retval = None
        if newpos is not None:
            curpos = self.algebraic_to_numeric(self.position)
            sameaxis = curpos[0] == newpos[0] or curpos[1] == newpos[1]
            if sameaxis and not curpos == newpos:
                retval = True
        return retval


class Bishop(object):
    """bishop chesspiece"""

    prefix = 'B'

    def is_legal_move(self, position):
        """
        :param position:
        :return:
        """

        newpos = self.algebraic_to_numeric(position)
        retval = None
        if newpos is not None:
            curpos = self.algebraic_to_numeric(self.position)
            if abs(curpos[0] - newpos[0]) == abs(curpos[1] - newpos[1]):
                retval = True
        return retval


class King(object):
    """king chesspiece"""

    prefix = 'K'

    def is_legal_move(self, position):
        """
        :param position:
        :return:
        """

        newpos = self.algebraic_to_numeric(position)
        retval = None
        if newpos is not None:
            curpos = self.algebraic_to_numeric(self.position)
            if abs(curpos[0] - newpos[0]) == 0 or 1 and \
                            abs(curpos[1] - newpos[1]) == 0 or 1:
                retval = True
        return retval


if __name__ == "__main__":
    rook = Rook('a1')