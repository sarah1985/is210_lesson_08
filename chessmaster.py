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
        if not self.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """convert position to ordered pair and vice versa"""

        coordinate = list(tile)
        conversion_dict = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
        }
        x = conversion_dict.get(coordinate[0])
        y = int(coordinate[1])
        position = (x, y)
        if x is None or y > 8:
            position = None

        return position

    def is_legal_move(self, position):
        """is move legal"""
        return self.algebraic_to_numeric(position) is not None

    def move(self, position):
        """move chesspiece"""

        if self.is_legal_move(self, position):

            current_move = (self.position, position, time.time)
            self.moves.append(current_move)
            self.position = position
        return current_move
