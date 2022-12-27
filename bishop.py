from piece import Piece
from move import Move

class Bishop(Piece):
    def __init__(self, side):
        Piece.__init__(self, side)
        self.image_file = side + '_bishop'

    def get_allowed_moves(self, row, col, turn_num, board_arr):
        dirc = [(1,1),(-1,1),(-1,-1),(1,-1)]
        allowed = self.gen_moves(row, col, board_arr, dirc)
        return allowed

    def get_moves(self, row, col, turn_num, board_arr):
        allowed = self.get_allowed_moves(row, col, turn_num, board_arr)
        valid = self.filter_check(row, col, board_arr, allowed)
        return valid