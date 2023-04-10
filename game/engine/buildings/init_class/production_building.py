from engine import t
from time import time
from . import Building

class ProductionBuilding(Building):
    def __init__(self, name, size, pos, angle, lvl, life, stock, layer):
        super().__init__(name, size, pos, angle, lvl, life, "production", stock, layer)
        self.start_production = True
        self.t = time()


    def check_product(self) -> bool:
        res = t.prod(self.name, self.lvl)
        for r in res["max"].items():
            if r[1] < self.stock.get(r[0]) + res["prod"][r[0]]:
                return False
        return True
    
    def update(self) -> None:
        prod = t.prod(self.name, self.lvl)
        if self.start_production and time() - self.t >= prod["time"] and self.check_product():
            for p in prod["prod"].items():
                self.stock[p[0]] += p[1]
                print(self.stock[p[0]])
                self.t = time()
