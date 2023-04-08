from .init_class import Building

class Barrack(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=0):
        super().__init__("Barrack", (2, 2), pos, angle, lvl, life, "formation", stock, layer)
        self.list_unit = []
        self.max = 5

    def former(self):
        pass