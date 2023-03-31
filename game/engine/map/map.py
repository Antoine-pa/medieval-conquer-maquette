import pygame
from engine import cst, t

class Map:
    def __init__(self):
        self.x = 1000 #nombre de case
        self.y = 1000
        self.pos = [self.x/2, self.y/2] #position actuelle de l'affichage dans la map
        self.list_build = [] #liste des batiments construits
        self.cases = [] #liste des coordonnées des cases occupées

    def __repr__(self):
        return f"Map :\n - taille : {self.x}x{self.y}\n - position : {self.pos}\n - bâtiments : {self.list_build}"

    def display(self, screen):
        """
        affichage de la map
        """
        screen.fill(cst("WHITE"))
        for x in range(0, cst("size_x")+int(cst("SIZE_CASE")), int(cst("SIZE_CASE"))):
            pygame.draw.line(screen, cst("BLACK"), (x-self.pos[0]%1*int(cst("SIZE_CASE")), 0), (x-self.pos[0]%1*int(cst("SIZE_CASE")), cst("size_y")))
            for y in range(0, cst("size_y")+int(cst("SIZE_CASE")), int(cst("SIZE_CASE"))):
                pygame.draw.line(screen, cst("BLACK"), (0, y-self.pos[1]%1*int(cst("SIZE_CASE"))), (cst("size_x"), y-self.pos[1]%1*int(cst("SIZE_CASE"))))
        for b in self.list_build:
            d = b.display(screen, *self.pos)
            if d and b.kind == "production" and b.start_production:
                if t.check_product(b):
                    color = cst("GREEN")
                else:
                    color = cst("RED")
                pygame.draw.rect(screen, color, pygame.Rect((b.pos[0]-self.pos[0])*int(cst("SIZE_CASE"))+cst("SIZE_CASE")//6, (b.pos[1]-self.pos[1])*int(cst("SIZE_CASE"))+cst("SIZE_CASE")//6, cst("SIZE_CASE")//6, cst("SIZE_CASE")//6), 0)
                
    def add_build(self, build):
        """
        ajout d'un bâtiment dans la liste des batiments et dans les cases occupées
        """
        self.list_build.append(build)
        for x in range(build.pos[0], build.pos[0]+build.size[0]):
            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                self.cases.append((x, y))
        if build.kind == "production":
            build.start_production = True
    
    def sup_build(self, build):
        self.list_build.remove(build)
        for x in range(build.pos[0], build.pos[0]+build.size[0]):
            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                self.cases.remove((x, y))
        del build
    
    def check_pos(self, build, cases_mem_tamp) -> int: #0 = libre, 1 = un batiment construit donc pas libre, 2 = un batiment posé, en memoire tampon donc pas libre
        """
        vérifie que la case est libre pour le bâtiment build
        """
        if tuple(build.pos) in cases_mem_tamp:
            return 2
        for x in range(build.pos[0], build.pos[0]+build.size[0]):
            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                if (x, y) in self.cases+cases_mem_tamp:
                    return 1
        return 0
    
    def reload_images(self):
        """
        recharge les images (après un zoom)
        """
        for b in self.list_build:
            b.load()
    
    def zoom(self, z):
        if z < 0 and cst("ZOOM") >= 1.1 or z > 0 and cst("ZOOM") <= 1.9:
            old_zoom = cst("ZOOM")
            t.set_const("ZOOM", round(cst("ZOOM") + z/10, 1))
            t.set_const("SIZE_CASE", 1/cst("ZOOM")*cst("SIZE_CASE")/(1/old_zoom))
            return True
        return False