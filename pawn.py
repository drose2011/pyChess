from piece import Piece
from move import Move

class Pawn(Piece):
    def __init__(self, side):
        Piece.__init__(self, side)
        self.image_file = side + '_pawn'
        self.side_mod = -1 if self.side == 'w' else 1
        self.doublejump = (False, -1)

    def get_allowed_moves(self, row, col, turn_num, board_arr):
        allowed = []
        if row + self.side_mod in range(8):
            if board_arr[row + self.side_mod][col] is None:
                allowed.append(Move((row, col), (row + self.side_mod, col)))

            if col + 1 in range(8) and \
               board_arr[row + self.side_mod][col + 1] is not None and \
               board_arr[row + self.side_mod][col + 1].get_side() != self.side:
                allowed.append(Move((row, col), (row + self.side_mod, col + 1)))

            if col - 1 in range(8) and \
               board_arr[row + self.side_mod][col - 1] is not None and \
               board_arr[row + self.side_mod][col - 1].get_side() != self.side:
                allowed.append(Move((row, col), (row + self.side_mod, col - 1)))

            # en passant
            if col + 1 in range(8) and \
               board_arr[row][col + 1] is not None and \
               isinstance(board_arr[row][col + 1], Pawn) and \
               board_arr[row][col + 1].doublejump[0] == True and \
               board_arr[row][col + 1].doublejump[1] == turn_num - 1:
                allowed.append(Move((row, col), (row + self.side_mod, col + 1, 1), ['enpassant', (row, col + 1)]))
            if col - 1 in range(8) and \
               board_arr[row][col - 1] is not None and \
               isinstance(board_arr[row][col - 1], Pawn) and \
               board_arr[row][col - 1].doublejump[0] == True and \
               board_arr[row][col - 1].doublejump[1] == turn_num - 1:
                allowed.append(Move((row, col), (row + self.side_mod, col - 1, 1), ['enpassant', (row, col - 1)]))

        # double jump
        if not self.hasMoved and \
           row + (2 * self.side_mod) in range(8) and \
           board_arr[row + self.side_mod][col] is None and \
           board_arr[row + (2 * self.side_mod)][col] is None:
            allowed.append(Move((row, col), (row + (2 * self.side_mod), col, 0), ['doublejump']))

        return allowed

    def get_moves(self, row, col, turn_num, board_arr):
        allowed = self.get_allowed_moves(row, col, turn_num, board_arr)
        return allowed
        # valid = self.filter_check(row, col, board_arr, allowed)


