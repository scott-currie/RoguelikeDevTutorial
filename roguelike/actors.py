class Actors(object):
    def __init__(self):
        self.player = None
        self.queue = []

    def get_actor_in_space(self, row, col):
        for actor in self.queue:
            if actor.row == row and actor.col == col:
                return actor
        return None
