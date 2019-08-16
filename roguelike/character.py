import abc
import logging
import tcod


class Character(object):
    def __init__(self, row, col):
        self.col = col
        self.col_next = col
        self.row = row
        self.row_next = row
        self.acted = False

    @abc.abstractmethod
    def update(self, kp, lvl_map, actors):
        pass

    def render(self):
        tcod.console_set_default_foreground(0, self.color)
        tcod.console_put_char(0, self.col, self.row,
                              self.symbol, tcod.BKGND_NONE)

    def move(self, row_dest, col_dest, lvl_map, actors):
        if lvl_map.space_is_legal(self.row_next, self.col_next):
            # Put terrain symbol back in vacant space
            lvl_map.render_at(self.row, self.col)
            # Make the space unoccupied
            # lvl_map.spaces[self.row][self.col].occupied = False
            # if lvl_map.spaces[self.row][self.col].terrain == '.':
            #     lvl_map.walkable[self.row][self.col] = True
            # Current position becomes next position
            self.row, self.col = self.row_next, self.col_next
            # Make space occupied
            # lvl_map.spaces[self.row][self.col].occupied = True
            # Space is not walkable if there's someone on it
            # lvl_map.walkable[self.row][self.col] = False
            # logging.debug(f'{self} acted to True')
            self.acted = True
        self.col_next, self.row_next = self.col, self.row

    def attack(self, enemy):
        print(self, 'attacked', enemy)
        enemy.hp -= self.atk
        self.acted = True
