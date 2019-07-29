from .character import Character
import tcod


class Player(Character):
    def __init__(self, x, y, atk, hp_max):
        super().__init__(x, y)
        self.symbol = '@'
        self.color = tcod.white
        self.atk = atk
        self.hp_max = hp_max
        self.hp = hp_max

    def get_dest(self, kp, lvl_map, actors):
        if kp.vk == tcod.KEY_DOWN:
            self.row_next += 1
        elif kp.vk == tcod.KEY_UP:
            self.row_next -= 1
        elif kp.vk == tcod.KEY_RIGHT:
            self.col_next += 1
        elif kp.vk == tcod.KEY_LEFT:
            self.col_next -= 1
        return self.row_next, self.col_next
