from roguelike.space import Space
import random

class Map():
    def __init__(self, rows, cols):
        self.height = rows
        self.width = cols
        self.spaces = self.make_spaces()
        self.make_walls()
        # self.make_obstacles()


    def make_spaces(self):
        ''' Generate and link space objects into map.spaces
        '''
        # Init spaces to a table of Nones
        # spaces = [[None for _ in range(self.width)] for _ in range(self.height)]
        spaces = []
        for row in range(self.height):
            # line holds items for this row
            line = []
            for col in range(self.width):
                spaces.append(line)
                new_space = Space(row, col)
                line.append(new_space)
                if row > 0:
                    # Link to space to the north
                    north = spaces[col][row - 1]
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
        print('Linked all the spaces!')
        return spaces


    def make_walls(self):
        for i in range(len(self.spaces)):
            for j in range(len(self.spaces[0])):
                if i == 0 or i == len(self.spaces) - 1:
                    self.spaces[i][j].terrain = '#'
                if j == 0 or j == len(self.spaces[i]) - 1:
                    self.spaces[i][j].terrain = '#'


    def make_obstacles(self):
        obstacles = set()
        n_obs = int((self.height - 2) * (self.width - 2) * .2) 
        while len(obstacles) < n_obs:
            print('Still making obstacles!')
            space = random.randint(1, self.width - 2), random.randint(1, self.height - 2)
            obstacles.add(space)
            print(len(obstacles))
            self.spaces[space[1]][space[0]].terrain = 'X'


    def space_is_in_bounds(self, x, y):
        if x > 0 and x < self.width - 1:
            if y > 0 and y < self.height - 1:
                return True
        return False
    
    
    def space_is_passable(self, x, y):
        return self.spaces[y][x].terrain == '.'


    def space_is_legal(self, x, y):
        return self.space_is_in_bounds(x, y) and self.space_is_passable(x, y)


    def get_random_legal_space(self):
        space = -1, -1
        while self.space_is_legal(space[0], space[1]):
            space = random.randint(1, self.width - 1), random.randint(1, self.height - 1)
            print('Finding legal space!')
        return space