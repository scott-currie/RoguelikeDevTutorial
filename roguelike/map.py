from roguelike.space import Space
import random
import sys
from tcod.map import Map as _Map
import numpy as np
import tcod.console


class Map(_Map):
    def __init__(self, cols, rows):
        super().__init__(rows, cols, order='C')
        self.height = rows
        self.width = cols
        self.spaces = self.make_spaces()
        self.make_walls()
        self.make_obstacles()

    def make_spaces(self):
        ''' Generate and link space objects into map.spaces
        '''
        print('Making spaces.')
        spaces = np.empty((self.height, self.width), dtype=Space)
        # Make a list of rows (height)
        for row in range(self.height):
            for col in range(self.width):
                spaces[row][col] = Space(col, row)
                self.walkable[row][col] = True
        print('Made spaces.')
        return spaces

    def make_walls(self):
        print('Making walls.')
        for row in range(self.height):
            for col in range(self.width):
                if (col == 0 or col == self.height - 1) or (row == 0 or row == self.width - 1):
                    self.spaces[row][col].terrain = '#'
                    self.walkable[row][col] = False
        print('Made walls.')

    def make_obstacles(self):
        print('Making obstacles.')
        obstacles = set()
        n_obs = int((self.height - 2) * (self.width - 2) * .2)
        while len(obstacles) < n_obs:
            space = random.randint(
                1, self.width - 2), random.randint(1, self.height - 2)
            obstacles.add(space)
            print(len(obstacles))
            self.spaces[space[1]][space[0]].terrain = 'X'
            self.walkable[space[1]][space[0]] = False
        print('Made obstaccles.')

    def space_is_in_bounds(self, row, col):
        if col >= 0 and col <= self.width - 1:
            if row >= 0 and row <= self.height - 1:
                return True
        return False

    def space_is_legal(self, row, col):
        return self.space_is_in_bounds(row, col) and self.walkable[row][col]

    def get_random_legal_space(self):
        while True:
            row, col = random.randint(
                1, self.height - 1), random.randint(1, self.width - 1)
            if self.space_is_legal(row, col):
                return (row, col)

    def render(self):
        for row in self.spaces:
            for space in row:
                tcod.console_put_char(0, space.col, space.row,
                                    space.terrain, tcod.BKGND_NONE)

    def render_at(self, row, col):
        # Draw terrain in current space
        tcod.console_set_default_foreground(0, tcod.yellow)
        tcod.console_put_char(0, col, row,
                                self.spaces[row][col].terrain, tcod.BKGND_NONE)        