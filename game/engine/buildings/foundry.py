from .init_class import ProductionBuilding

class Foundry(Building):
    def __init__(self, x, y):
        super().__init__("Foundry", (), [], 1, 100, "production")