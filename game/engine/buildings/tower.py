from .init_class import Building

class Tower(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=0):
        super().__init__("Tower", (3, 3), pos, angle, lvl, life, "defense", {"bois": 20}, layer)
