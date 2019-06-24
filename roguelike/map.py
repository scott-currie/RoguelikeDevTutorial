from roguelike.space import Space
import random

class Map():
    def __init__(self, rows, cols):
        self.height = rows
        self.width = cols
        self.spaces = self.make_spaces(rows, cols)
        self.terrain = [['.'] * cols for _ in range(rows)]
        self.make_walls()
        self.make_obstacles()


    def make_spaces(self, rows, cols):
        spaces = [[None for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                spaces[row][col] = Space(row, col)
        return spaces

    def make_walls(self):
        for i in range(len(self.terrain)):
            for j in range(len(self.terrain[0])):
                if i == 0 or i == len(self.terrain) - 1:
                    self.terrain[i][j] = '#'
                if j == 0 or j == len(self.terrain[i]) - 1:
                    self.terrain[i][j] = '#'


    def make_obstacles(self):
        obstacles = set()
        n_obs = int((self.height - 2) * (self.width - 2) * .2) 
        while len(obstacles) < n_obs:
            space = random.randint(1, self.width - 2), random.randint(1, self.height - 2)
            obstacles.add(space)
            self.terrain[space[1]][space[0]] = 'X'


    def space_is_in_bounds(self, x, y):
        if x > 0 and x < self.width - 1:
            if y > 0 and y < self.height - 1:
                return True
        return False
    
    
    def space_is_passable(self, x, y):
        return self.terrain[y][x] == '.'


    def space_is_legal(self, x, y):
        return self.space_is_in_bounds(x, y) and self.space_is_passable(x, y)
