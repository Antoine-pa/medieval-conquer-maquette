from engine import t
from .init_class import ProductionBuilding

class Field(ProductionBuilding):
    def __init__(self, pos, angle=0, lvl=1, life=100, layer=0):
        super().__init__("Field", (2, 2), pos, angle, lvl, life, {"cereals": 0}, layer)