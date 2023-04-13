from .init_class import ResourceTransportation
from engine import t, cst

class EntranceGallery(ResourceTransportation):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=-1, t=None):
        super().__init__("EntranceGallery", (1, 1), pos, angle, lvl, life, "transport", {"bois":50, "acier" : 20}, layer, 2, 5, t)