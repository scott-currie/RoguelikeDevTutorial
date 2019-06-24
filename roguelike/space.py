class Space(object):
    def __init__(self, row, col, terrain='.'):
        self.x = col
        self.y = row
        self.terrain = terrain