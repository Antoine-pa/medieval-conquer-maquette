from .init_class import Building

class Cannon(Building):
    def __init__(self, x, y):
        super().__init__("Canon", (3, 3), [x, y], 1, 100, "defense")
        self.type = ""
        self.deg = 0