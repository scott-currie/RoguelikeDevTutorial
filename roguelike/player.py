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

    def update(self, kp, lvl_map, actors):
        self.acted = False
        # logging.debug('About to move.')
        # Check if destination has an enemy
        enemy = actors.get_actor_in_space(self.row, self.col)
        if enemy:
            self.attack(enemy)
            self.acted = True
            print('Whack!')
        else:
            self.move(kp, lvl_map, actors)
        # logging.debug('About to render.')
        self.render()
        # logging.debug(f'{self} acted to False')
        # self.acted = False


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
