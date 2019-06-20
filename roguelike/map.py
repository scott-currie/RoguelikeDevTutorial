class Map():
    def __init__(self, rows, cols):
        self.grid = [['.'] * cols for _ in range(rows)]
