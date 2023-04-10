from time import time
from engine import t
from .init_class import ProductionBuilding

class Field(ProductionBuilding):
    def __init__(self, pos, angle=0, lvl=1, life=100, layer=0):
        super().__init__("Field", (2, 2), pos, angle, lvl, life, {"cereals": 0}, layer)
        self.t = time()

    def update(self):
        prod = t.prod(self.name, self.lvl)
        if self.start_production and time() - self.t >= prod["time"] and self.check_product():
            self.stock["cereals"] += prod["prod"]["cereals"]
            print(self.stock["cereals"])
            self.t = time()