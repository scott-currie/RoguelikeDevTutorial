import abc
import logging
import tcod


class Character(object):
    def __init__(self, row, col, atk, hp_max, name):
        self.col = col
        self.col_next = col
        self.row = row
        self.row_next = row
        self.acted = False
        self.alive = True
        self.atk = atk
        self.hp_max = hp_max
        self.hp = hp_max
        self.name = name

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
            # Space we are leaving becomes walkable again
            lvl_map.walkable[self.row][self.col] = True
            # Current position becomes next position
            self.row, self.col = self.row_next, self.col_next
            self.acted = True
        # Next and current are the same space
        self.col_next, self.row_next = self.col, self.row

    def attack(self, enemy):
        print('Whack!', self.name, 'attacked', enemy.name, 'for',
              self.atk, 'HP leaving them', enemy.hp, 'remaining.')
        enemy.hp -= self.atk
        enemy.check_hp()
        self.acted = True

    def check_hp(self):
        if self.hp <= 0:
            self.alive = False
