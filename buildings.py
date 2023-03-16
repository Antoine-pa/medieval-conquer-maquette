import pygame
from tools import t, cst

class Building:
    """
    class Building:
        class de base de tout les bâtiments
    """
    def __init__(self, name, size, pos, life):
        self.name = name
        self.img = None
        self.size = size
        self.pos = pos
        self.angle = 0
        self.life = life
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


class UsineArmeSiege(Building):
    def __init__(self, x, y):
        super().__init__("UsineArmeSiege", (2, 2), [x, y], 100)
        self.list_bat = []
        self.max = 2

    def construire(self):
        pass

class Canon(Building):
    def __init__(self, x, y):
        super().__init__("Canon", (3, 3), [x, y], 100)
        self.type = ""
        self.deg = 0

class Grenier(Building):
    def __init__(self, x, y):
        super().__init__("Grenier", (3, 3), [x, y], 100)
        self.ress = {}

class Reserve(Building):
    def __init__(self, x, y):
        super().__init__("Reserve", (3, 3), [x, y], 100)
        self.ress = {}

class Muraille(Building):
    def __init__(self, x, y):
        super().__init__("Muraille", (1, 1), [x, y], 400)
        self.ress = {}

class Tour(Building):
    def __init__(self, x, y):
        super().__init__("Tour", (3, 3), [x, y], 100)
        self.ress = {}

class Champs(Building):
    def __init__(self, x, y):
        super().__init__("Champs", (2, 2), [x, y], 100)
        self.ress = {}

class Caserne(Building):
    def __init__(self, x, y):
        super().__init__("Caserne", (2, 2), [x, y], 100)
        self.list_unit = []
        self.max = 5

    def former(self):
        pass
DICT_BUILDINGS = {"Caserne" : Caserne, "Champs" : Champs, "Grenier" : Grenier, "Tour" : Tour, "Muraille" : Muraille, "Reserve" : Reserve}