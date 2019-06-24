from .character import Character
# from roguelike.character import Character

class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol = '@'