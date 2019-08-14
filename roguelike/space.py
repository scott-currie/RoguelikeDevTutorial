class Space(object):
    def __init__(self, col, row, terrain='.'):
        self.col = col
        self.row = row
        self.terrain = terrain
        self.walkable = True
        self.occupied = False
