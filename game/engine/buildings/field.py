from time import time
from .init_class import Building

class Field(Building):
    def __init__(self, x, y):
        super().__init__("Fields", (2, 2), [x, y], 1, 100, "production")
        self.res = {"cereals": 0}
        self.start_production = False
        self.t = time()

    def update(self):
        prod = t.prod(self.name, self.lvl)
        if self.start_production and time() - self.t >= prod["time"] and t.check_product(self):
            self.res["cereals"] += prod["prod"]["cereals"]
            print(self.res["cereals"])
            self.t = time()