from .init_class import Building

class Barrack(Building):
    def __init__(self, x, y):
        super().__init__("Barrack", (2, 2), [x, y], 1, 100, "formation")
        self.list_unit = []
        self.max = 5

    def former(self):
        pass