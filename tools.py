import json
import pygame
from functools import lru_cache
init_res = {"bois" : {"max" : 100,"stock" : 75},"fer" : {"max" : 200,"stock" : 60},"eau" : {"max" : 100,"stock" : 60},"acier" : {"max" : 200,"stock" : 30},"or" : {"max" : 60,"stock" : 12},"charbon" : {"max" : 120,"stock" : 79}}
class Tools:
    def __init__(self):
        self.data = self.reload_data()
        self.data_cost = self.load_cost()
        self.data_res = self.load_res()
        self.data_prod = self.load_production()
        self.cst = self.const

    def load_img(self, name, x, y):
        img = pygame.image.load(name)
        img = pygame.transform.scale(img,(x, y))
        return img
    
    def check_res(self, resources : dict, resources2 : dict = {}):
        for r in resources.items():
            if r[1]+resources2.get(r[0], 0) > self.res(r[0])["stock"]:
                return r[0]
        return True

    def load_cost(self):
        with open("cost.json", "r") as f:
            data = json.load(f)
        return data
    
    def load_res(self):
        with open("resources.json", "r") as f:
            data = json.load(f)
        return data

    def reload_data(self):
        with open("const.json", "r") as f:
            data = json.load(f)
        return data

    def load_production(self):
        with open("production.json", "r") as f:
            data = json.load(f)
        return data

    @lru_cache(maxsize=None)
    def prod(self, name, lvl):
        r = self.data_prod[name][str(lvl)]
        return r

    @lru_cache(maxsize=None)
    def cost(self, name, lvl):
        r = self.data_cost[name][str(lvl)]
        return r

    @lru_cache(maxsize=None)
    def res(self, name):
        r = self.data_res[name]
        return r

    @lru_cache(maxsize=None)
    def const(self, name):
        r = self.data[name]
        return r

    def set_res(self, name, val):
        self.res.cache_clear()
        self.data_res[name]["stock"] = val
        with open("resources.json", "w") as f:
            f.write(json.dumps(self.data_res, indent=4))

    def set_const(self, name, val):
        self.const.cache_clear()
        if isinstance(val, tuple):
            val = list(val)
        self.data[name] = val
        with open("const.json", "w") as f:
            f.write(json.dumps(self.data, indent=4))

    def add_new_res(self, name, m, val):
        self.res.cache_clear()
        self.data_res[name] = {"max" : m, "stock" : val}
        with open("resources.json", "w") as f:
            f.write(json.dumps(self.data_res, indent=4))

    def set_all_const(self, size_x, size_y):
        self.set_const("size_x", size_x)
        self.set_const("size_y", size_y)
        self.set_const("BLACK", (0, 0, 0))
        self.set_const("RED", (150, 0, 0))
        self.set_const("GREEN", (0, 150, 0))
        self.set_const("WHITE", (255, 255, 255))
        self.set_const("GREY_WHITE", (200, 200, 200))
        self.set_const("GREY_YELLOW", (232, 222, 100))
        self.set_const("RED_ORANGE", (235, 50, 30))
        self.set_const("GREY", (100, 100, 100))
        self.set_const("SENSIBILITY", 0.4) #sensibilité d'un déplacement (en case de la map)
        self.set_const("MENU_EDIT_POS", (size_x-3*size_y//16, 15*size_y//16, 3*size_y//16, size_y//16)) #position du menu d'edit, MENU_EDIT_POS[3] correspond aussi à la longueur d'une case
        self.set_const("LONG_BLOCK_MENU_EDIT", 3*self.cst("MENU_EDIT_POS")[3]//4) #longueur du contenu d'une case du menu d'edit
        self.set_const("GAP_BLOCK_COL_MENU_EDIT", self.cst("MENU_EDIT_POS")[3]//8) #espace entre le contenu et le bord d'une case du menu d'eedit
        self.set_const("POS_BUTTONS_MENU_EDIT", (((self.cst("MENU_EDIT_POS")[3])-self.cst("LONG_BLOCK_MENU_EDIT"))//2, (self.cst("MENU_EDIT_POS")[1])+(size_y-(self.cst("MENU_EDIT_POS"))[1])//2-self.cst("LONG_BLOCK_MENU_EDIT")//2)) #
        self.set_const("LIST_BAT_MENU_EDIT", ["Caserne", "Fields", "Grenier", "Tour", "Muraille", "Reserve"])
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

    def check_product(self, build) -> bool:
        res = self.prod(build.name, build.lvl)
        for r in res["max"].items():
            if r[1] < build.res[r[0]] + res["prod"][r[0]]:
                return False
        return True

t = Tools()
for r in init_res.items():
    t.add_new_res(r[0], r[1]["max"], r[1]["stock"])
def cst(name):
    return t.cst(name)