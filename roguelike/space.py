class Space(object):
    def __init__(self, col, row, terrain='.'):
        self.col = col
        self.row = row
        self.terrain = terrain
        self.n = None
        self.s = None
        self.e = None
        self.w = None
