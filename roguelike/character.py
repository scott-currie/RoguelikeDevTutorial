import abc
import tcod

class Character(object):
    def __init__(self, row, col):
        self.col = col
        self.col_next = col
        self.row = row
        self.row_next = row
        self.loc = self.row, self.col

    def render(self):
        tcod.console_set_default_foreground(0, tcod.white)
        tcod.console_put_char(0, self.col, self.row,
                              self.symbol, tcod.BKGND_NONE)

    @abc.abstractmethod
    def move(self, lvl_map, kp=None):
        self.row_next, self.col_next = self.get_dest(kp)
        # Do self move if next position dfferent than current
        if lvl_map.space_is_legal(self.row_next, self.col_next):
            # Put terrain symbol back in vacant space
            lvl_map.render_at(self.row, self.col)
            # Current position becomes next position
            self.row, self.col = self.row_next, self.col_next
        else:
            print(f'Can\'t go to {self.row_next, self.col_next}')
        self.col_next, self.row_next = self.col, self.row