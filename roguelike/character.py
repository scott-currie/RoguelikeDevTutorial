class Character(object):
    def __init__(self, row, col):
        self.col = col
        self.col_prev = -1
        self.col_next = -1
        self.row = row
        self.row_prev = -1
        self.row_next = -1
        self.loc = self.row, self.col

    def move(self, dest_row, dest_col):
        self.col = dest_col
        self.row = dest_row
