from .init_class import Building

class Granary(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=0):
        super().__init__("Granary", (3, 3), pos, angle, lvl, life, "stockage", stock, layer)