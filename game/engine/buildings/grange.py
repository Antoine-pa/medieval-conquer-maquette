from .init_class import Building

class Grange(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}):
        super().__init__("Grange", (3, 3), pos, angle, lvl, life, "stockage", stock)