from roguelike.space import Space
import random
import sys


class Map():
    def __init__(self, rows, cols):
        self.height = rows
        self.width = cols
        self.spaces = self.make_spaces()
        self.make_walls()
        self.print_terrain()
        self.make_obstacles()

    def make_spaces(self):
        ''' Generate and link space objects into map.spaces
        '''
        print('Making spaces.')
        spaces = []
        # Make a list of rows (height)
        for row in range(self.height):
            # line holds items for this row
            line = []
            spaces.append(line)
            for col in range(self.width):

                new_space = Space(col, row)
                line.append(new_space)
                if row > 0:
                    # Link to space to the north
                    north = spaces[row - 1][col]
                    new_space.n = north
                    # If there is a space to the north, link it to new_space
                    if north is not None:
                        north.s = new_space
                if col > 0:
                    # Link space to the west
                    west = line[col - 1]
                    new_space.w = west
                    # If there's a space to the west, link it to new_space
                    if west is not None:
                        west.e = new_space
        print('Made spaces.')
        return spaces

    def make_walls(self):
        print('Making walls.')
        for row in range(len(self.spaces)):
            for col in range(len(self.spaces[0])):
                if (col == 0 or col == self.height - 1) or (row == 0 or row == self.width - 1):
                    self.spaces[row][col].terrain = '#'
                    print(f'wall@({row},{col})')
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
        print('Made obstaccles.')

    def space_is_in_bounds(self, row, col):
        if col > 0 and col < self.width - 1:
            if row > 0 and row < self.height - 1:
                return True
        return False

    def space_is_passable(self, row, col):
        return self.spaces[row][col].terrain == '.'

    def space_is_legal(self, row, col):
        return self.space_is_in_bounds(row, col) and self.space_is_passable(row, col)

    def get_random_legal_space(self):
        while True:
            row, col = random.randint(
                1, self.height - 1), random.randint(1, self.width - 1)
            if self.space_is_legal(row, col):
                return (row, col)

    def print_terrain(self):
        for row in self.spaces:
            for space in row:
                sys.stdout.write(space.terrain + ' ')
            sys.stdout.write('\n')
