class Space(object):
    def __init__(self, row, col, terrain='.'):
        self.x = col
        self.y = row
        self.loc = (self.x, self.y)
        self.terrain = terrain
        self.n = None
        self.s = None
        self.e = None
        self.w = None