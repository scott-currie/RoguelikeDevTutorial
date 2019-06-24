class Character(object):
    def __init__(self, x, y):
        self.x = x
        self.x_prev = -1
        self.y = y
        self.y_prev = -1

    def move(self, dest_x, dest_y):
        self.x = dest_x
        self.y = dest_y