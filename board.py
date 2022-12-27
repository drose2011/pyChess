from time import sleep
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from piece import Piece
from move import Move

# TODO: enpessant, castle, not duplicating board each time, check checking

class Board:

    starting_boards = {'default':  [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
                                    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                                    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']],
                       'test_1':   [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    [None, None, None, None, None, None, None, None],
                                    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]}

    def __init__(self, board='default'):
        self.turn_num = 0
        self.turn = 'w'
        self.init_board(self.starting_boards[board])
        self.selected_piece = None
        self.allowed_moves = []

    def new_piece(self, piece_str):
        if piece_str is None:
            return None
        piece_side = piece_str[0]
        piece_type = piece_str[1]
        piece = None
        if piece_type == 'p':
            return Pawn(piece_side)
        elif piece_type == 'r':
            return Rook(piece_side)
        elif piece_type == 'n':
            return Knight(piece_side)
        elif piece_type == 'b':
            return Bishop(piece_side)
        elif piece_type == 'q':
            return Queen(piece_side)
        elif piece_type == 'k':
            return King(piece_side)

    def init_board(self, start_board):
        self.board_arr = [[None for _ in range(8)] for _ in range(8)]
        for row_idx in range(8):
            for col_idx in range(8):
                self.board_arr[row_idx][col_idx] = self.new_piece(start_board[row_idx][col_idx])

    def move(self, move):
        move.start_row
        self.selected_piece = None
        self.allowed_moves = []
        self.board_arr[move.end_row][move.end_col] = self.board_arr[move.start_row][move.start_col]
        self.board_arr[move.start_row][move.start_col] = None
        self.board_arr[move.end_row][move.end_col].hasMoved = True
        if move.special is not None:
            if move.special[0] == 'doublejump':
                self.board_arr[move.end_row][move.end_col].doublejump = (True, self.turn_num)
            elif move.special[0] == 'enpassant':
                remove_row = move.special[1][0]
                remove_col = move.special[1][1]
                self.board_arr[remove_row][remove_col] = None
            elif move.special[0] == 'castle':
                pass # TODO

        self.turn = 'b' if self.turn == 'w' else 'w'
        self.turn_num += 1
        
    def check_game_over(self):
        # if self.turn == 'b':
        #     return 1
        return 0

    def get_board(self):
        return (self.board_arr, self.selected_piece, self.allowed_moves)

    def clicked(self, row, col):
        if self.selected_piece is not None and Move(self.selected_piece, (row, col)) in self.allowed_moves:
            for move in self.allowed_moves:
                if Move(self.selected_piece, (row, col)) == move:
                    self.move(move)
                    break
            self.selected_piece = None
            self.allowed_moves = []
        else:
            self.selected_piece = None
            self.allowed_moves = []
            if self.board_arr[row][col] is not None:
                clicked_piece_side = self.board_arr[row][col].get_side()
                if self.turn == clicked_piece_side:
                    self.selected_piece = (row, col)
                    self.allowed_moves = self.board_arr[row][col].get_moves(row, col, self.turn_num, self.board_arr)


    def comp_move_next(self):
        return False
        if self.turn == 'b':
            return True
        return False

    def move_AI(self):
        sleep(3)
        self.board_arr[0][0] = None
        