from .init_class import ResourceTransportation
from engine import t, cst
import time
import random

class Gallery(ResourceTransportation):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=-1, t=None):
        super().__init__("Gallery", (1, 1), pos, angle, lvl, life, "transport", {}, layer, 2, 5, t)
