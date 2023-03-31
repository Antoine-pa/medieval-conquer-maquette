from .init_class import Building

class Tower(Building):
    def __init__(self, x, y):
        super().__init__("Tower", (3, 3), [x, y], 1, 100, "defense")