class Character(object):
    def __init__(self, row, col):
        self.col = col
        self.col_next = col
        self.row = row
        self.row_next = row
        self.loc = self.row, self.col

    def move(self, dest_row, dest_col):
        self.col = dest_col
        self.row = dest_row
