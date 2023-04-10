from .init_class import Building

class Gallery(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=-1):
        super().__init__("Gallery", (1, 1), pos, angle, lvl, life, "stockage", stock, layer)