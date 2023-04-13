import pygame
from engine import t, cst

class Building:
    """
    class Building:
        class de base de tout les bâtiments
    """
    def __init__(self, name, size, pos, angle, lvl, life, kind, stock, layer):
        self.name = name
        self.img = None
        self.img_alpha = None
        self.size = size
        self.pos = pos
        self.lvl = lvl
        self.angle = angle
        self.life = life
        self.kind = kind
        self.stock = stock
        self.layer = layer
        if name not in cst("LIST_JUNCTION_BUILDING"):
            self.load()

    def __repr__(self):
        return f"{self.name} : (position : {self.pos}; taille : {self.size}; vie : {self.life}); angle : {self.angle}; stock : {self.stock}"
    
    def in_windows(self, x:int, y:int) -> bool:
        return x-2 <=self.pos[0] <= cst("size_x")/int(cst("SIZE_CASE"))+x and y-2 <=self.pos[1] <= cst("size_y")/int(cst("SIZE_CASE"))+y

    def display(self, screen:pygame.surface.Surface, x:int, y:int, alpha:bool = False) -> bool:
        """
        calcul si le bâtiment est affiché ou non et l'affiche
        """
        if self.in_windows(x, y):
            if alpha:
                img = self.img_alpha
            else:
                img = self.img
            screen.blit(img, ((self.pos[0]-x)*int(cst("SIZE_CASE")), (self.pos[1]-y)*int(cst("SIZE_CASE"))))
            return True
        return False

    def load(self) -> None:
        """
        charge l'image du bâtiment
        """
        self.img = t.load_img(f"buildings/{self.name}/{self.name}.png", int(cst("SIZE_CASE"))*self.size[0] , int(cst("SIZE_CASE"))*self.size[1], 255)
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.img_alpha = t.load_img(f"buildings/{self.name}/{self.name}.png", int(cst("SIZE_CASE"))*self.size[0] , int(cst("SIZE_CASE"))*self.size[1], 32)
        self.img_alpha = pygame.transform.rotate(self.img_alpha, self.angle)
    
    def rotate(self, angle:int) -> None:
        self.angle += angle
        self.angle %= 360
        self.load()


class Canon(Building):
    def __init__(self, x, y):
        super().__init__("Canon", (3, 3), [x, y], 1, 100, "defense")
        self.type = ""
        self.deg = 0

class UsineArmeSiege(Building):
    def __init__(self, x, y):
        super().__init__("UsineArmeSiege", (2, 2), [x, y], 1, 100, "formation")
        self.list_bat = []
        self.max = 2

    def construire(self):
        pass


class Foundry(Building):
    def __init__(self, x, y):
        super().__init__("Foundry", (), [], 1, 100, "production")