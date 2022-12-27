from move import Move

class Piece:
    def __init__(self, side):
        self.hasMoved = False
        self.side = side

    def get_side(self):
        return self.side

    def gen_moves(self, row, col, board_arr, dirc, dist_limit=8):
        allowed = []

        dist = 1
        while len(dirc) > 0 and dist <= dist_limit:
            idx = 0
            while idx < len(dirc):
                move = dirc[idx]
                tmp_row = row + dist * move[0]
                tmp_col = col + dist * move[1]
                if tmp_row not in range(8) or tmp_col not in range(8):
                    del dirc[idx]
                    idx -= 1
                elif board_arr[tmp_row][tmp_col] is not None:
                    if board_arr[tmp_row][tmp_col].side != board_arr[row][col].side:
                        allowed.append(Move((row, col), (tmp_row, tmp_col)))
                    del dirc[idx]
                    idx -= 1
                else:
                    allowed.append(Move((row, col), (tmp_row, tmp_col)))
                idx += 1
            dist += 1
        return allowed

    def filter_check(self, row, col, board_arr, allowed):
        return allowed
        # for move in allowed:
        #     (row, col) = move
