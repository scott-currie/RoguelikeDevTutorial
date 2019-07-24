from .character import Character
from .player import Player
import tcod


class Monster(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = 'M'
        self.color = tcod.red

    def get_dest(self, kp, lvl_map, actors):
        '''Find the next space to reach the player.'''
        # for actor in actors:
        #     if isinstance(actor, Player):
        #         player = actor
        if self.is_adjacent_player(actors.player):
            return self.row, self.col
        astar = tcod.path.AStar(lvl_map)
        _path = astar.get_path(self.col, self.row, actors.player.col, actors.player.row)
        print(_path)
        return _path[0][1], _path[0][0]

    def is_adjacent_player(self, player):
        if self.col >= player.col - 1 and self.col <= player.col + 1:
            if self.row >= player.row - 1 and self.row <= player.row + 1:
                return True
        return False
