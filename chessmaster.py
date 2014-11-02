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
        x_axis = conversion_dict.get(coordinate[0])
        y_axis = int(coordinate[1]) - 1
        position = (x_axis, y_axis)
        if x_axis is None or y_axis > 7:
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


class Bishop(ChessPiece):
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


class King(ChessPiece):
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


class ChessMatch(object):
    """logs chess match"""

    def __init__(self, pieces=None):
        """catalogs dictionary of pieces"""

        if pieces is not None:
            self.pieces = pieces
            self.log = []

        else:
            self.reset()

    def reset(self):
        """reset pieces"""

        self.pieces = {
            'Ra1': Rook('a1'),
            'Rh1': Rook('h1'),
            'Ra8': Rook('a8'),
            'Rh8': Rook('h8'),
            'Bc1': Bishop('c1'),
            'Bf1': Bishop('f1'),
            'Bc8': Bishop('c8'),
            'Bf8': Bishop('f8'),
            'Ke1': King('e1'),
            'Ke8': King('e8')
            }

    def move(self, full_notation, newpos):
        """stores moves"""

        new_move = self.pieces[full_notation].move(newpos)
        if new_move:
            self.log.append()
            self.pieces[prefix + newpos] = self.pieces.pop(full_notation)
        else:
            return False

    def __len__(self):
        """length of log"""

        return len(self.log)


if __name__ == "__main__":
    rook = Rook('a1')