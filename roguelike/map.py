class Map():
    def __init__(self, rows, cols):
        self.height = rows
        self.width = cols
        self.terrain = [['.'] * cols for _ in range(rows)]
        self.make_walls()


    def make_walls(self):
        for i in range(len(self.terrain)):
            for j in range(len(self.terrain[0])):
                if i == 0 or i == len(self.terrain) - 1:
                    self.terrain[i][j] = '#'
                if j == 0 or j == len(self.terrain[i]) - 1:
                    self.terrain[i][j] = '#'

    def space_is_in_bounds(self, x, y):
        if x > 0 and x < self.width - 1:
            if y > 0 and y < self.height - 1:
                return True
        return False
    
    
    def space_is_passable(self, x, y):
        return self.terrain[y][x] == '.'


    def space_is_legal(self, x, y):
        print(f'Checking if {x},{y} is legal.')
        return self.space_is_in_bounds(x, y) and self.space_is_passable(x, y)