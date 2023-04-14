from .init_class import ProductionBuilding

class FactoryWeaponHeadquarters(ProductionBuilding):
    def __init__(self, x, y):
        super().__init__("UsineArmeSiege", (2, 2), [x, y], 1, 100, "formation")
        self.list_bat = []
        self.max = 2

    def construire(self):
        pass