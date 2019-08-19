from roguelike.character import Character
from roguelike.player import Player
import logging
import random
import tcod



class Monster(Character):
    def __init__(self, x, y, atk, hp_max):
        super().__init__(x, y)
        self.symbol = 'M'
        # self.color = tcod.red
        self.color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.atk = atk
        self.hp_max = hp_max
        self.hp = hp_max
        logging.debug(f'{self} created at row={self.row}, col={self.col}')

    def update(self, kp, lvl_map, actors):
        self.acted = False
        # Toggle monster's space walkable for pathfinding
        lvl_map.walkable[self.row][self.col] = True
        # logging.debug('About to move.')
        if self.is_adjacent_player(actors.player):
            self.attack(actors.player)
        else:
            self.row_next, self.col_next = self.get_dest(lvl_map, actors)
            # Check next space is unoccupied
            if not actors.get_actor_in_space(self.row_next, self.col_next):
                self.move(self.row_next, self.col_next, lvl_map, actors)
            else:
                # No one to fight and our next space is occupied
                self.acted = True
        # logging.debug('About to render.')
        lvl_map.walkable[self.row][self.col] = False
        self.render()
        # logging.debug(f'{self} acted to False')
        ('Monster update. Acted=', self.acted)

    def get_dest(self, lvl_map, actors):
        '''Find the next space to reach the player.'''
        # lvl_map.walkable[self.row][self.col] = True
        if self.is_adjacent_player(actors.player):
            return self.row, self.col
        astar = tcod.path.AStar(lvl_map)
        # logging.debug(f'{self} @ row={self.row}, col={self.col}')
        # logging.debug(f'{actors.player} @ row={actors.player.row}, col={actors.player.col}')
        _path = astar.get_path(
            self.col, self.row, actors.player.col, actors.player.row)
        print(_path)
        # lvl_map.walkable[self.row][self.col] = False
        if _path:
            return _path[0][1], _path[0][0]
        return self.row, self.col

    def is_adjacent_player(self, player):
        if self.col >= player.col - 1 and self.col <= player.col + 1:
            if self.row >= player.row - 1 and self.row <= player.row + 1:
                return True
        return False
