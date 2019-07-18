from .character import Character
import tcod

class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = '@'
        self.color = tcod.white

    def get_dest(self, kp, lvl_map, actors):
        print('Getting player destination.')
        if kp.vk == tcod.KEY_DOWN:
            self.row_next += 1
        elif kp.vk == tcod.KEY_UP:
            self.row_next -= 1
        elif kp.vk == tcod.KEY_RIGHT:
            self.col_next += 1
        elif kp.vk == tcod.KEY_LEFT:
            self.col_next -= 1
        return self.row_next, self.col_next
