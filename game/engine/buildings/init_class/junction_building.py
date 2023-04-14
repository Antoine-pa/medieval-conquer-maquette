from . import Building
import pygame
from engine import t, cst

class JunctionBuilding(Building):
    def __init__(self, name, size, pos, angle, lvl, life, kind, stock, layer, t = None):
        super().__init__(name, size, pos, angle, lvl, life, kind, stock, layer)
        if t is None:
            self.t = [0, 0, 0, 0]
        else:
            self.t = t
        self.load()

    def add_junction(self, list_dict_pos_build:list) -> None:
        list_build = self.get_build_adj(list_dict_pos_build)
        for b in list_build:
            if b.pos[0] <= self.pos[0] < b.pos[0] + b.size[0]:
                if b.pos[1] < self.pos[1]: #positionnement en bas d'une autre muraille
                    self.t[1] = 1
                    if isinstance(b, JunctionBuilding):
                        b.t[3] = 1
                elif b.pos[1] > self.pos[1]: #positionnement en haut d'une autre muraille
                    self.t[3] = 1
                    if isinstance(b, JunctionBuilding):
                        b.t[1] = 1
            elif b.pos[1] <= self.pos[1] < b.pos[1] + b.size[1]:
                if b.pos[0] > self.pos[0]: #positionnement à gauche d'une autre muraille
                    self.t[0] = 1
                    if isinstance(b, JunctionBuilding):
                        b.t[2] = 1
                elif b.pos[0] < self.pos[0]: #positionnement à droite d'une autre muraille
                    self.t[2] = 1
                    if isinstance(b, JunctionBuilding):
                        b.t[0] = 1
        list_build.append(self)
        for b in list_build:
            if isinstance(b, JunctionBuilding):
                b.rotate_junction()
    
    def del_junction(self, list_dict_pos_build:list) -> None:
        list_build = self.get_build_adj(list_dict_pos_build)
        for b in list_build:
            if isinstance(b, JunctionBuilding):
                if b.pos[0] == self.pos[0] and b.pos[1]  < self.pos[1]: #positionnement en bas d'une autre muraille
                    b.t[3] = 0
                elif b.pos[0] == self.pos[0] and b.pos[1]  > self.pos[1]: #positionnement en haut d'une autre muraille
                    b.t[1] = 0
                elif b.pos[0] > self.pos[0] and b.pos[1]  == self.pos[1]: #positionnement à gauche d'une autre muraille
                    b.t[2] = 0
                elif b.pos[0] < self.pos[0] and b.pos[1]  == self.pos[1]: #positionnement à droite d'une autre muraille
                    b.t[0] = 0
        for b in list_build:
            if isinstance(b, JunctionBuilding):
                b.rotate_junction()

    def get_build_adj(self, list_dict_pos_build:list) -> list:
        pos = []
        for x in range(2):
            pos.append((self.pos[0] -1+x*(2), self.pos[1]))
            pos.append((self.pos[0], self.pos[1] -1+x*(2)))
        list_build = []
        for p in pos:
            for dict_pos_build in list_dict_pos_build:
                b = dict_pos_build.get(p)
                if b is not None and b.name in cst("DICT_JUNCTIONS")[self.name]:
                    list_build.append(b)
        return list_build
    
    def get_suffix(self) -> str:
        if sum(self.t) != 2:
            suffix = str(sum(self.t))
        else:
            if self.t[0] == self.t[2] and self.t[1] == self.t[3]:
                suffix = "2_0"
            else:
                suffix = "2_1"
        return suffix

    def load(self) -> None:
        """
        charge l'image du bâtiment
        """
        name = self.name + self.get_suffix()
        self.img = t.load_img(f"buildings/{self.name}/{name}.png", int(cst("SIZE_CASE")) * self.size[0], int(cst("SIZE_CASE")) * self.size[1], 255)
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.img_alpha = t.load_img(f"buildings/{self.name}/{name}.png", int(cst("SIZE_CASE"))*self.size[0] , int(cst("SIZE_CASE"))*self.size[1], 32)
        self.img_alpha = pygame.transform.rotate(self.img_alpha, self.angle)

    def rotate_junction(self) -> None:
        if sum(self.t) == 1:
            self.angle = self.t.index(1)*90
        elif sum(self.t) == 3:
            self.angle = self.t.index(0)*90
        elif sum(self.t) == 2:
            if self.t[0] == self.t[2] and self.t[1] == self.t[3]:
                self.angle = self.t.index(1) * 90
            else:
                if self.t[0] == self.t[3] == 1:
                    self.angle = 270
                else:
                    self.angle = self.t.index(1)*90
        self.load()
