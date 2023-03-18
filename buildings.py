import pygame
from tools import t, cst
from time import time

class Building:
    """
    class Building:
        class de base de tout les bâtiments
    """
    def __init__(self, name, size, pos, lvl, life, kind):
        self.name = name
        self.img = None
        self.size = size
        self.pos = pos
        self.lvl = lvl
        self.angle = 0
        self.life = life
        self.kind = kind
        self.load()

    def __repr__(self):
        return f"{self.name} : (position : {self.pos}; taille : {self.size}; vie : {self.life})"
    
    def in_windows(self, x, y):
        return x-2 <=self.pos[0] <= cst("size_x")/int(cst("SIZE_CASE"))+x and y-2 <=self.pos[1] <= cst("size_y")/int(cst("SIZE_CASE"))+y

    def display(self, screen, x, y):
        """
        calcul si le bâtiment est affiché ou non et l'affiche
        """
        if self.in_windows(x, y):
            screen.blit(self.img, ((self.pos[0]-x)*int(cst("SIZE_CASE")), (self.pos[1]-y)*int(cst("SIZE_CASE"))))
            return True
        return False

    def load(self):
        """
        charge l'image du bâtiment
        """
        self.img = t.load_img(f"./assets/buildings/{self.name}.png", int(cst("SIZE_CASE"))*self.size[0] , int(cst("SIZE_CASE"))*self.size[1])
        self.img = pygame.transform.rotate(self.img, self.angle)
    
    def rotate(self, angle):
        self.angle += angle
        self.angle %= 360
        self.load()


class Canon(Building):
    def __init__(self, x, y):
        super().__init__("Canon", (3, 3), [x, y], 1, 100, "defense")
        self.type = ""
        self.deg = 0

class Grenier(Building):
    def __init__(self, x, y):
        super().__init__("Grenier", (3, 3), [x, y], 1, 100, "stockage")
        self.res = {}

class Reserve(Building):
    def __init__(self, x, y):
        super().__init__("Reserve", (3, 3), [x, y], 1, 100, "stockage")
        self.res = {}

class Muraille(Building):
    def __init__(self, x, y):
        super().__init__("Muraille", (1, 1), [x, y], 1, 400, "defense")

class Tour(Building):
    def __init__(self, x, y):
        super().__init__("Tour", (3, 3), [x, y], 1, 100, "defense")

class Fields(Building):
    def __init__(self, x, y):
        super().__init__("Fields", (2, 2), [x, y], 1, 100, "production")
        self.res = {"cereals" : 0}
        self.start_production = False
        self.t = time()
    
    def update(self):
        prod = t.prod(self.name, self.lvl)
        if self.start_production and time() - self.t >= prod["time"] and t.check_product(self):
            self.res["cereals"] += prod["prod"]["cereals"]
            self.t = time()
            print(self.res)



class UsineArmeSiege(Building):
    def __init__(self, x, y):
        super().__init__("UsineArmeSiege", (2, 2), [x, y], 1, 100, "formation")
        self.list_bat = []
        self.max = 2

    def construire(self):
        pass


class Caserne(Building):
    def __init__(self, x, y):
        super().__init__("Caserne", (2, 2), [x, y], 1, 100, "formation")
        self.list_unit = []
        self.max = 5

    def former(self):
        pass
DICT_BUILDINGS = {"Caserne" : Caserne, "Fields" : Fields, "Grenier" : Grenier, "Tour" : Tour, "Muraille" : Muraille, "Reserve" : Reserve}