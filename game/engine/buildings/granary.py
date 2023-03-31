from .init_class import Building

class Granary(Building):
    def __init__(self, x, y):
        super().__init__("Granary", (3, 3), [x, y], 1, 100, "stockage")
        self.res = {}