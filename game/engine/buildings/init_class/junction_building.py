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

    def del_junction(self, list_build):
        builds_changing = []
        for b in list_build:
            if b != self and ((abs(b.pos[0] - self.pos[0]) == 1 and abs(b.pos[1] - self.pos[1]) == 0) or (abs(b.pos[0] - self.pos[0]) == 0 and abs(b.pos[1] - self.pos[1]) == 1)):
                if b.pos[0] == self.pos[0] and b.pos[1]  < self.pos[1]: #positionnement en bas d'une autre muraille
                    b.t[3] = 0
                elif b.pos[0] == self.pos[0] and b.pos[1]  > self.pos[1]: #positionnement en haut d'une autre muraille
                    b.t[1] = 0
                elif b.pos[0] > self.pos[0] and b.pos[1]  == self.pos[1]: #positionnement à gauche d'une autre muraille
                    b.t[2] = 0
                elif b.pos[0] < self.pos[0] and b.pos[1]  == self.pos[1]: #positionnement à droite d'une autre muraille
                    b.t[0] = 0
                builds_changing.append(b)
        t.rotate_wall(builds_changing)

    
    def add_junction(self, list_build):
        builds_changing = []
        for b in list_build:
            if b != self and ((abs(b.pos[0] - self.pos[0]) == 1 and abs(b.pos[1] - self.pos[1]) == 0) or (abs(b.pos[0] - self.pos[0]) == 0 and abs(b.pos[1] - self.pos[1]) == 1)):
                if b.pos[0] == self.pos[0] and b.pos[1] < self.pos[1]: #positionnement en bas d'une autre muraille
                    self.t[1] = 1
                    b.t[3] = 1
                elif b.pos[0] == self.pos[0] and b.pos[1] > self.pos[1]: #positionnement en haut d'une autre muraille
                    self.t[3] = 1
                    b.t[1] = 1
                elif b.pos[0] > self.pos[0] and b.pos[1] == self.pos[1]: #positionnement à gauche d'une autre muraille
                    self.t[0] = 1
                    b.t[2] = 1
                elif b.pos[0] < self.pos[0] and b.pos[1]  == self.pos[1]: #positionnement à droite d'une autre muraille
                    self.t[2] = 1
                    b.t[0] = 1
                builds_changing.append(b)
        builds_changing.append(self)
        for b in builds_changing:
            b.rotate_junction()

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

    def load(self) -> None:
        """
        charge l'image du bâtiment
        """
        if sum(self.t) != 2:
            name = self.name + str(sum(self.t))
        else:
            if self.t[0] == self.t[2] and self.t[1] == self.t[3]:
                name = self.name + "2_0"
            else:
                name = self.name + "2_1"
        self.img = t.load_img(f"buildings/{self.name}/{name}.png", int(cst("SIZE_CASE")) * self.size[0] - 1, int(cst("SIZE_CASE")) * self.size[1] - 1, 255)
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.img_alpha = t.load_img(f"buildings/{self.name}/{name}.png", int(cst("SIZE_CASE"))*self.size[0]-1 , int(cst("SIZE_CASE"))*self.size[1]-1, 32)
        self.img_alpha = pygame.transform.rotate(self.img_alpha, self.angle)
