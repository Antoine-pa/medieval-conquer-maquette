from engine import t
from . import Building

class ProductionBuilding(Building):
    def __init__(self, name, size, pos, angle, lvl, life, stock, layer):
        super().__init__(name, size, pos, angle, lvl, life, "production", stock, layer)
        self.start_production = True


    def check_product(self) -> bool:
        res = t.prod(self.name, self.lvl)
        for r in res["max"].items():
            if r[1] < self.stock.get(r[0]) + res["prod"][r[0]]:
                return False
        return True
    
    def update(self):
        """
        méthode à faire pour remplacer l'update de Field et de toutes les autres class production.
        """
        pass