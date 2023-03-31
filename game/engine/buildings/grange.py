from .init_class import Building

class Grange(Building):
    def __init__(self, x, y):
        super().__init__("Grange", (3, 3), [x, y], 1, 100, "stockage")
        self.res = {}