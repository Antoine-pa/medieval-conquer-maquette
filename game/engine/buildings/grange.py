from .init_class import Building

class Grange(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=0):
        super().__init__("Grange", (3, 3), pos, angle, lvl, life, "stockage", stock, layer)