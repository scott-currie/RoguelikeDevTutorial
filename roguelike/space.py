class Space(object):
    def __init__(self, col, row, terrain='.'):
        self.col = col
        self.row = row
        # self.loc = (self.x, self.y)
        self.terrain = terrain
        self.n = None
        self.s = None
        self.e = None
        self.w = None
