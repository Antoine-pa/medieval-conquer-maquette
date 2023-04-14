from .init_class import Building

class Cannon(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=0):
        super().__init__("Cannon", (2, 2), pos, angle, lvl, life, "defense", stock, layer)
        self.type = ""
        self.deg = 0