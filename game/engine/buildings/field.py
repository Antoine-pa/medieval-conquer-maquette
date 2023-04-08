from time import time
from .init_class import Building

class Field(Building):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={"cereals": 0}, layer=0):
        super().__init__("Field", (2, 2), pos, angle, lvl, life, "production", layer)
        self.start_production = False
        self.t = time()

    def update(self):
        prod = t.prod(self.name, self.lvl)
        if self.start_production and time() - self.t >= prod["time"] and t.check_product(self):
            self.stock["cereals"] += prod["prod"]["cereals"]
            print(self.stock["cereals"])
            self.t = time()