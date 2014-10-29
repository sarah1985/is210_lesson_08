#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: The Chess Piece"""

import time


class ChessPiece(object):
    """chess piece class"""

    prefix = ""

    def __init__(self, position):
        self.position = position
        self.moves = []
        if not self.is_legal_move():
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

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
        if x is None or y > 8:
            position = None

        return position

    def is_legal_move(position):
        """is move legal"""
        return self.algebraic_to_numeric(position) is not None

    def move(self, position):
        """move chesspiece"""

        if self.is_legal_move():

            current_move = (ChessPiece.prefix + self.position, ChessPiece.prefix + position, time.time)
            self.moves.append(current_move)
            self.position = position
            return current_move

        else:
            return False


class Rook(object):
    """rook chesspiece"""


class Bishop(object):
    """bishop chesspiece"""



class King(object):
    """king chesspiece"""