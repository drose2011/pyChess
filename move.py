class Move:
    def __init__(self, start, end, special=None):
        self.start_row = start[0]
        self.start_col = start[1]
        self.end_row = end[0]
        self.end_col = end[1]
        self.special = special

    def __eq__(self, other):
        if self.start_row == other.start_row and \
           self.start_col == other.start_col and \
           self.end_row == other.end_row and \
           self.end_col == other.end_col:
            return True
        return False
