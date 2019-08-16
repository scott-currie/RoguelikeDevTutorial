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
        # Find out what space (if any) player wants to move to
        self.row_next, self.col_next = self.get_dest(kp, lvl_map, actors)
        # Check to see if the destination is different than current position
        if self.row_next != self.row or self.col_next != self.col:
            # Check if destination has an enemy
            enemy = actors.get_actor_in_space(self.row_next, self.col_next)
            if enemy:
                self.attack(enemy)
            else:
                self.move(self.row_next, self.col_next, lvl_map, actors)
        # logging.debug('About to render.')
        self.render()
        # logging.debug(f'{self} acted to False')

    def get_dest(self, kp, lvl_map, actors):
        row_next, col_next = self.row, self.col
        if kp.vk == tcod.KEY_DOWN:
            row_next += 1
        elif kp.vk == tcod.KEY_UP:
            row_next -= 1
        elif kp.vk == tcod.KEY_RIGHT:
            col_next += 1
        elif kp.vk == tcod.KEY_LEFT:
            col_next -= 1
        return row_next, col_next
