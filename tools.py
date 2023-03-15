import json
import pygame
from functools import lru_cache

class Tools:
    def __init__(self):
        self.data = self.reload_data()
        self.cst = self.const

    def load_img(self, name, x, y):
        img = pygame.image.load(name)
        img = pygame.transform.scale(img,(x, y))
        return img

    def reload_data(self):
        with open("const.json", "r") as f:
            data = json.load(f)
        return data
        
    @lru_cache
    def const(self, name):
        r = self.data.get(name, None)
        return r
    
    def set_const(self, name, val):
        self.const.cache_clear()
        if isinstance(val, tuple):
            val = list(val)
        self.data[name] = val
        with open("const.json", "w") as f:
            f.write(json.dumps(self.data, indent=4))

    def set_all_const(self, size_x, size_y):
        self.set_const("size_x", size_x)
        self.set_const("size_y", size_y)
        self.set_const("BLACK", (0, 0, 0))
        self.set_const("RED", (150, 0, 0))
        self.set_const("WHITE", (255, 255, 255))
        self.set_const("GREY_WHITE", (200, 200, 200))
        self.set_const("GREY", (100, 100, 100))
        self.set_const("SENSIBILITY", 0.4)
        self.set_const("MENU_EDIT_POS", (5*size_x//6, size_y//2, size_x//6, size_y//2))
        self.set_const("LONG_COL_MENU_EDIT", self.cst("MENU_EDIT_POS")[2] // 3)
        self.set_const("LONG_BLOCK_MENU_EDIT", 2*self.cst("LONG_COL_MENU_EDIT")//3)
        self.set_const("GAP_BLOCK_COL_MENU_EDIT", self.cst("LONG_COL_MENU_EDIT")//6)
        self.set_const("POS_Y_BOTTOM_MENU_EDIT", self.cst("MENU_EDIT_POS")[1]+7*(size_y-self.cst("MENU_EDIT_POS")[1])//8)
        self.set_const("LONG_BUTTON_MENU_EDIT", 3*(size_y-self.cst("POS_Y_BOTTOM_MENU_EDIT"))//4)
        self.set_const("POS_BUTTONS_MENU_EDIT", ((self.cst("LONG_COL_MENU_EDIT")-self.cst("LONG_BUTTON_MENU_EDIT"))//2, self.cst("POS_Y_BOTTOM_MENU_EDIT")+(size_y-self.cst("POS_Y_BOTTOM_MENU_EDIT"))//2-self.cst("LONG_BUTTON_MENU_EDIT")//2))
        self.set_const("LIST_BAT_MENU_EDIT", ["Caserne", "Champs", "Grenier", "Tour", "Muraille", "Reserve"])
        self.set_const("ZOOM", 1)
        self.set_const("SIZE_CASE", 50)
        self.set_const("SIZE_TEXT", 30)

    def text(self, screen, text, color, pos: tuple, size):
        """
        fonction pour afficher du text
        """
        FONT = pygame.font.Font("./assets/fonts/Melon Honey.ttf", size)
        screen.blit(FONT.render(text, True, color), pos)
        del FONT

    def barre(self, screen, pos : tuple, size : tuple, ratio : float, color : tuple):
        """
        fonction permettant d'afficher une barre de progression (ex : menu d'affichage des ressources)
        """
        pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], size[0]*ratio, size[1]), 0)
        pygame.draw.rect(screen, cst("BLACK"), pygame.Rect(pos[0], pos[1], size[0], size[1]), 1)

    def get_case(self, pos, _map):
        """
        calcul de la case sur laquelle la souris est
        """
        place_x = int((pos[0]+_map.pos[0]*int(cst("SIZE_CASE")))//int(cst("SIZE_CASE")))
        place_y = int((pos[1]+_map.pos[1]*int(cst("SIZE_CASE")))//int(cst("SIZE_CASE")))
        return (place_x, place_y)

t = Tools()

def cst(name):
    return t.cst(name)