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

    @abc.abstractmethod
    def update(self, kp, lvl_map, actors):
        pass

    def render(self):
        tcod.console_set_default_foreground(0, self.color)
        tcod.console_put_char(0, self.col, self.row,
                              self.symbol, tcod.BKGND_NONE)

    @abc.abstractmethod
    def move(self, kp, lvl_map, actors):
        # Where do you want to go?
        self.row_next, self.col_next = self.get_dest(kp, lvl_map, actors)
        # Nowhere? Go back.
        if self.row_next == self.row and self.col_next == self.col:
            return
        # Try to move
        if lvl_map.space_is_legal(self.row_next, self.col_next):
            # Put terrain symbol back in vacant space
            lvl_map.render_at(self.row, self.col)
            # Current position becomes next position
            self.row, self.col = self.row_next, self.col_next
            # logging.debug(f'{self} acted to True')
            self.acted = True
        self.col_next, self.row_next = self.col, self.row


    def attack(self, enemy):
        print(self, 'attacked', enemy)
        enemy.hp -= self.atk
        self.acted = True