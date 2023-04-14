from .init_class import ResourceTransportation
from engine import t, cst

class ExitGallery(ResourceTransportation):
    def __init__(self, pos, angle=0, lvl=1, life=100, stock={}, layer=-1, t=None):
        super().__init__("ExitGallery", (1, 1), pos, angle, lvl, life, "transport", {}, layer, 2, 5, t)

    def exit(self, _map, ress: dict) -> None:
        b = _map.dict_pos_build[0].get(tuple(self.pos))
        if b is None:
            b = self
        for r in ress.items():
            if r[0] not in b.stock:
                b.stock[r[0]] = 0
            b.stock[r[0]] += r[1]
        print(b)
