import abc
import logging
import tcod


class Character(object):
    def __init__(self, row, col):
        self.col = col
        self.col_next = col
        self.row = row
        self.row_next = row
        self.loc = self.row, self.col
        self.acted = False

    def update(self, kp, lvl_map, actors):
        self.acted = False
        logging.debug('About to move.')
        self.move(kp, lvl_map, actors)
        logging.debug('About to render.')
        self.render()
        logging.debug(f'{self} acted to False')
        # self.acted = False

    def render(self):
        tcod.console_set_default_foreground(0, self.color)
        tcod.console_put_char(0, self.col, self.row,
                              self.symbol, tcod.BKGND_NONE)

    @abc.abstractmethod
    def move(self, kp, lvl_map, actors):
        # moved = False
        self.row_next, self.col_next = self.get_dest(kp, lvl_map, actors)
        # if not hasattr(self, 'is_adjacent_player'):
        #     if (self.row_next, self.col_next) == (self.row, self.col):
        #         return False
        # Do self move if next position dfferent than current
        if hasattr(self, 'is_adjacent_player'):
            if self.is_adjacent_player(actors.player):
                self.acted = True
                return
        else:
            if self.row_next == self.row and self.col_next == self.col:
                return
        if lvl_map.space_is_legal(self.row_next, self.col_next):
            # Put terrain symbol back in vacant space
            lvl_map.render_at(self.row, self.col)
            # Current position becomes next position
            self.row, self.col = self.row_next, self.col_next
            # moved = True
            logging.debug(f'{self} acted to True')
            self.acted = True
        else:
            print(f'Can\'t go to {self.row_next, self.col_next}')
        self.col_next, self.row_next = self.col, self.row
        # return moved
