from .init_class import JunctionBuilding
from engine import t, cst

class EntranceGallery(JunctionBuilding):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=0, t=None):
        super().__init__("EntranceGallery", (1, 1), pos, angle, lvl, life, "forwarding", stock, layer, t)