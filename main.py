import pygame
import time
import json
from buildings import *
from tools import t

def cst(name):
    return t.cst(name)

pygame.init()
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w-100,screen_info.current_h-100))
size_x = screen_info.current_w-100
size_y = screen_info.current_h-100

def set_all_const(size_x, size_y):
    t.set_const("size_x", size_x)
    t.set_const("size_y", size_y)
    t.set_const("BLACK", (0, 0, 0))
    t.set_const("RED", (150, 0, 0))
    t.set_const("WHITE", (255, 255, 255))
    t.set_const("GREY_WHITE", (200, 200, 200))
    t.set_const("GREY", (100, 100, 100))
    t.set_const("SENSIBILITY", 0.4)
    t.set_const("MENU_EDIT_POS", (5*size_x//6, size_y//2, size_x//6, size_y//2))
    t.set_const("LONG_COL_MENU_EDIT", cst("MENU_EDIT_POS")[2] // 3)
    t.set_const("LONG_BLOCK_MENU_EDIT", 2*cst("LONG_COL_MENU_EDIT")//3)
    t.set_const("GAP_BLOCK_COL_MENU_EDIT", cst("LONG_COL_MENU_EDIT")//6)
    t.set_const("POS_Y_BOTTOM_MENU_EDIT", cst("MENU_EDIT_POS")[1]+7*(size_y-cst("MENU_EDIT_POS")[1])//8)
    t.set_const("LONG_BUTTON_MENU_EDIT", 3*(size_y-cst("POS_Y_BOTTOM_MENU_EDIT"))//4)
    t.set_const("POS_BUTTONS_MENU_EDIT", ((cst("LONG_COL_MENU_EDIT")-cst("LONG_BUTTON_MENU_EDIT"))//2, cst("POS_Y_BOTTOM_MENU_EDIT")+(size_y-cst("POS_Y_BOTTOM_MENU_EDIT"))//2-cst("LONG_BUTTON_MENU_EDIT")//2))
    t.set_const("LIST_BAT_MENU_EDIT", ["Caserne", "Champs", "Grenier", "Tour", "Muraille", "Reserve"])
    t.set_const("ZOOM", 1)
    t.set_const("SIZE_CASE", 50)
    t.set_const("SIZE_TEXT", 30)

set_all_const(size_x, size_y)

class Map:
    def __init__(self):
        self.x = 1000 #nombre de case
        self.y = 1000
        self.pos = [self.x/2, self.y/2] #position actuelle de l'affichage dans la map
        self.list_build = [] #liste des batiments construits
        self.cases = [] #liste des coordonnées des cases occupées
        self.add_build(Caserne(503, 506)) #ajout d'une caserne

    def __repr__(self):
        return f"Map :\n - taille : {self.x}x{self.y}\n - position : {self.pos}\n - bâtiments : {self.list_build}"

    def display(self):
        """
        affichage de la map
        """
        screen.fill(cst("WHITE"))
        for x in range(0, size_x+int(cst("SIZE_CASE")), int(cst("SIZE_CASE"))):
            pygame.draw.line(screen, cst("BLACK"), (x-self.pos[0]%1*int(cst("SIZE_CASE")), 0), (x-self.pos[0]%1*int(cst("SIZE_CASE")), size_y))
            for y in range(0, size_y+int(cst("SIZE_CASE")), int(cst("SIZE_CASE"))):
                pygame.draw.line(screen, cst("BLACK"), (0, y-self.pos[1]%1*int(cst("SIZE_CASE"))), (size_x, y-self.pos[1]%1*int(cst("SIZE_CASE"))))
        for b in self.list_build:
            b.display(screen, *self.pos)
    
    def add_build(self, build):
        """
        ajout d'un bâtiment dans la liste des batiments et dans les cases occupées
        """
        self.list_build.append(build)
        for x in range(build.pos[0], build.pos[0]+build.size[0]):
            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                self.cases.append((x, y))
    
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

class Button:
    """
    class Button:
        classe gérant la conception de bouttons
    """
    def __init__(self, coords: tuple, text: str, thickness: int):
        self.coords = coords
        self.text = text
        self.thickness = thickness
    
    def __repr__(self):
        return f"coords : {self.coords}, text : {self.text}, thickness : {self.thickness}"

    def collidepoint(self, pos) -> bool:
        """
        check si le click est sur le boutton
        """
        return self.coords[0] <= pos[0] <= self.coords[2] and self.coords[1] <= pos[1] <= self.coords[3]

    def pos_text(self) -> tuple: #à modifier, marche pas vraiment
        """
        retourne la position du texte à afficher
        """
        return (self.coords[0]+self.thickness+3, self.coords[3]-self.thickness-1.25*cst("SIZE_TEXT"))
    
    def display(self, screen):
        """
        affiche le boutton
        """
        pygame.draw.rect(screen, cst("BLACK"), (self.coords[0], self.coords[1], self.coords[2] - self.coords[0], self.coords[3] - self.coords[1]), self.thickness)
        Text(self.text, cst("BLACK"), self.pos_text(), cst("SIZE_TEXT"))
        
class Menu:
    """
    class Menu:
        classe gérant toutes les interfaces non jouables:
        - settings
        - menu de construction
        - affichage des ressources

    """
    def __init__(self):
        self.action = "map"
        self.mem_tamp = None #variable de mémoire temporaire
        self.buttons = {} #liste des bouttons affichés
    
    def __repr__(self):
        return f"Menu :\n - action : {self.action}\n - memoire tampon : {self.mem_tamp}\n - boutons : {self.buttons}"

    def set_action(self, act : str):
        """
        fonction permettant de changer de section du menu
        """
        if self.action != act:
            self.action = act
        else:
            self.action = "map"
        self.update_mem_tamp()
        self.update_buttons()

    def update_buttons(self):
        self.buttons = {}
        if self.action in ("edit-add", "edit-sup"):
            self.buttons["edit_validation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BUTTON_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BUTTON_MENU_EDIT")), "yes", 1)
            self.buttons["edit_annulation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_COL_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BUTTON_MENU_EDIT")+cst("LONG_COL_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BUTTON_MENU_EDIT")), "no", 1)
        elif self.action == "edit":
            self.buttons["edit_construction"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BUTTON_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BUTTON_MENU_EDIT")), "con", 1)
            self.buttons["edit_destruction"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_COL_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BUTTON_MENU_EDIT")+cst("LONG_COL_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BUTTON_MENU_EDIT")), "des", 1)
            self.buttons["edit_validation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+2*cst("LONG_COL_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BUTTON_MENU_EDIT")+2*cst("LONG_COL_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BUTTON_MENU_EDIT")), "yes", 1)


    def update_mem_tamp(self):
        if self.action.startswith("edit"):
            if self.mem_tamp is None:
                self.mem_tamp = {"bat" : None, "list_bat" : {"add" : {"pos" : [], "bat" : []}, "sup" : []}, "ress" : {}}
        else:
            self.mem_tamp = None


    def display(self, screen, ressources : dict, pos_map: list):
        """
        fonction permettant d'afficher les zones des sections du menu
        """
        if self.action == "map":
            pass
        elif self.action.startswith("edit"):
            self.display_edit(screen, pos_map)
        elif self.action == "settings":
            self.display_settings(screen)
        elif self.action == "ressources":
            self.display_ressources(screen, ressources)
        for button in self.buttons.items():
            button[1].display(screen)
    
    def display_edit(self, screen, pos_map: list):
        """
        fonction permettant d'afficher le menu d'edition de la map
        """
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(*cst("MENU_EDIT_POS")), 0)
        for i in range(len(cst("LIST_BAT_MENU_EDIT"))//3):
            for j in range(3):
                img = t.load_img("./assets/buildings/"+cst("LIST_BAT_MENU_EDIT")[3*i+j]+".png", cst("LONG_BLOCK_MENU_EDIT"), cst("LONG_BLOCK_MENU_EDIT"))
                pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0] + (i+1)*cst("LONG_COL_MENU_EDIT"), cst("MENU_EDIT_POS")[1]), (cst("MENU_EDIT_POS")[0]+ (i+1)*cst("LONG_COL_MENU_EDIT"), cst("POS_Y_BOTTOM_MENU_EDIT")))
                screen.blit(img, (cst("MENU_EDIT_POS")[0] + j*cst("LONG_COL_MENU_EDIT") + cst("GAP_BLOCK_COL_MENU_EDIT"), cst("MENU_EDIT_POS")[1] + i*cst("LONG_COL_MENU_EDIT") + cst("GAP_BLOCK_COL_MENU_EDIT")))
        pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0], cst("POS_Y_BOTTOM_MENU_EDIT")), (size_x, cst("POS_Y_BOTTOM_MENU_EDIT")))
        for b in self.mem_tamp["list_bat"]["add"]["bat"]:
            b.display(screen, *pos_map)

    def display_ressources(self, screen, ressources : dict): #à faire : créer les constantes au début pour éviter les calculs
        """
        fonction permettant d'afficher les ressources
        """
        screen.fill(cst("BLACK"))
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(size_x//4, size_y//4, size_x//2, size_y//2), 0)
        ressources = list(ressources.items())
        for i in range(len(ressources)):
            res = ressources[i]
            ratio = res[1][1] / res[1][0]
            barre((size_x/2-size_x/16, size_y*(3*len(ressources)+2+6*i)/(12*len(ressources))), (size_x/8, size_y/(6*len(ressources))), ratio, cst("RED"))
            Text(res[0], cst("BLACK"), (size_x/4+size_x/16, size_y/4+size_y/(6*len(ressources))+i*size_y/(2*len(ressources))), int(size_y/(6*len(ressources))))
            Text(str(res[1][1])+"/"+str(res[1][0])+" ("+str(round(ratio*100, 2))+"%)", cst("BLACK"), (size_x/2+size_x/8, size_y/4+size_y/(6*len(ressources))+i*size_y/(2*len(ressources))), int(size_y/(6*len(ressources))))

    def display_settings(self, screen):
        """
        fonction permettant d'afficher les paramètres du jeu
        """
        screen.fill(cst("BLACK"))
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(size_x//4, size_y//4, size_x//2, size_y//2), 0)




def barre(pos : tuple, size : tuple, ratio : float, color : tuple):
    """
    fonction permettant d'afficher une barre de progression (ex : menu d'affichage des ressources)
    """
    pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], size[0]*ratio, size[1]), 0)
    pygame.draw.rect(screen, cst("BLACK"), pygame.Rect(pos[0], pos[1], size[0], size[1]), 1)

def Text(text, color, pos: tuple, size):
    """
    fonction pour afficher du text
    """
    FONT = pygame.font.Font("./assets/fonts/Melon Honey.ttf", size)
    screen.blit(FONT.render(text, True, color), pos)
    del FONT

class Game:
    """
    class Game:
        class gérant la map et les menu
    """
    def __init__(self):
        self._map = Map()
        self._menu = Menu()
        self.ressources = {"bois" : (100, 75), "fer" : (200, 60), "eau" : (100, 60), "feu" : (60, 40), "acier" : (200, 30), "or" : (60, 12), "charbon" : (120, 79)}

    def __repr__(self):
        return f"Game :\n - {self._map}\n\n - {self._menu}\n\n - ressources : {self.ressources}"

    def display(self, screen):
        """
        gère l'affichage du jeu
        """
        if self._menu.action == "map" or self._menu.action.startswith("edit"):
            self._map.display()
        self._menu.display(screen, self.ressources, self._map.pos)
        pygame.display.update()

    def deplacement(self, x, y):
        """
        gère les déplacement dans la map
        """
        self._map.pos[0] += x
        self._map.pos[1] += y
    
    def reload_images(self):
        """
        lance le rechargement des images
        """
        self._map.reload_images()
        if self._menu.mem_tamp is not None:
            for b in self._menu.mem_tamp["list_bat"]["add"]["bat"]:
                b.load()
    
    def get_case(self, pos):
        """
        calcul de la case sur laquelle la souris est
        """
        place_x = int((pos[0]+self._map.pos[0]*int(cst("SIZE_CASE")))//int(cst("SIZE_CASE")))
        place_y = int((pos[1]+self._map.pos[1]*int(cst("SIZE_CASE")))//int(cst("SIZE_CASE")))
        return (place_x, place_y)

game = Game()
continuer = True
DICT_BUILDINGS = {"Caserne" : Caserne, "Champs" : Champs, "Grenier" : Grenier, "Tour" : Tour, "Muraille" : Muraille, "Reserve" : Reserve}
while continuer:
    game.display(screen) #on affiche le jeu
    for event in pygame.event.get():
        try:
            pos = list(pygame.mouse.get_pos())
        except : pass
        if event.type == pygame.KEYDOWN: #à l'appui d'une touche
            k = pygame.key.get_pressed()
            if game._menu.action == "map" or game._menu.action.startswith("edit"):
                # dépacement sur la map
                if k[pygame.K_d]:
                    game._map.pos[0] += cst("SENSIBILITY")
                elif k[pygame.K_s]:
                    game._map.pos[1] += cst("SENSIBILITY")
                elif k[pygame.K_z]:
                    game._map.pos[1] -= cst("SENSIBILITY")
                elif k[pygame.K_q]:
                    game._map.pos[0] -= cst("SENSIBILITY")
        elif event.type == pygame.MOUSEWHEEL:
            #scroll pour le zoom
            event.y = -event.y
            if event.y < 0 and cst("ZOOM") >= 1.1 or event.y > 0 and cst("ZOOM") <= 1.9:
                old_zoom = cst("ZOOM")
                t.set_const("ZOOM", round(cst("ZOOM") + event.y/10, 1))
                t.set_const("SIZE_CASE", 1/cst("ZOOM")*cst("SIZE_CASE")/(1/old_zoom))
                game.reload_images()
        elif event.type == pygame.MOUSEBUTTONUP and event.__dict__["button"] == 1: #lors d'un clic gauche
            if game._menu.action.startswith("edit"): #si un edit est en cours
                if game._menu.mem_tamp is not None and (not cst("MENU_EDIT_POS")[0] < pos[0] or not cst("MENU_EDIT_POS")[1] < pos[1]): #si le clic est sur la map
                    place_x, place_y = game.get_case(pos) #récupération des cases
                    if game._menu.action == "edit-add" and game._menu.mem_tamp["bat"] is not None: #si un bâtiment à construire est séléctionné
                        #construction bâtiment
                        build = DICT_BUILDINGS[game._menu.mem_tamp["bat"]["bat"]](place_x, place_y) #on instancie le bâtiment
                        build.rotate(game._menu.mem_tamp["bat"]["angle"])
                        place = game._map.check_pos(build, game._menu.mem_tamp["list_bat"]["add"]["pos"])
                        if place == 0: #on vérifie que la place est libre
                            game._menu.mem_tamp["list_bat"]["add"]["bat"].append(build) #on ajoute le bâtiment dans la mémoire tampon
                            for x in range(build.pos[0], build.pos[0]+build.size[0]):
                                for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                    game._menu.mem_tamp["list_bat"]["add"]["pos"].append((x, y))
                        elif place == 2: #annuler la construction d'un batiment
                            for b in game._menu.mem_tamp["list_bat"]["add"]["bat"]:
                                for x in range(b.pos[0], b.pos[0]+b.size[0]):
                                    for y in range(b.pos[1], b.pos[1]+b.size[1]):
                                        if (place_x, place_y) == (x, y):
                                            build = b
                            for x in range(build.pos[0], build.pos[0]+build.size[0]):
                                for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                    game._menu.mem_tamp["list_bat"]["add"]["pos"].remove((x, y))
                            game._menu.mem_tamp["list_bat"]["add"]["bat"].remove(build)
                        else:
                            del build
                    elif game._menu.action == "edit-sup":
                        #destruction d'un bâtiment
                        build = None
                        for b in game._map.list_build:
                            for x in range(b.pos[0], b.pos[0]+b.size[0]):
                                for y in range(b.pos[1], b.pos[1]+b.size[1]):
                                    if (place_x, place_y) == (x, y):
                                        build = b
                        if build is not None:
                            game._menu.mem_tamp["list_bat"]["sup"].append(build)
                #sélection bâtiment
                elif cst("MENU_EDIT_POS")[0] < pos[0] and cst("MENU_EDIT_POS")[1] < pos[1] < cst("POS_Y_BOTTOM_MENU_EDIT") : #si le clic est dans le menu d'edition
                    if game._menu.action == "edit-add":
                        pos[0], pos[1] = pos[0] - cst("MENU_EDIT_POS")[0], pos[1] - cst("MENU_EDIT_POS")[1]
                        coord_case = (int(pos[0]/cst("LONG_COL_MENU_EDIT")), int(pos[1]/cst("LONG_COL_MENU_EDIT"))) #on calcul les coordonnées de la case
                        index = 3*coord_case[1] + coord_case[0] #on calcul l'index de la case dans la liste des bâtiments
                        game._menu.mem_tamp["bat"] = {"bat" : cst("LIST_BAT_MENU_EDIT")[index], "angle" : 0} #on ajoute le bâtiment à la mémoire tampon dans la section réservé au bâtiment séléctinné pour de la construction
            for button in game._menu.buttons.items():
                if button[1].collidepoint(pos):
                    if button[0] == "edit_validation":
                        if game._menu.action == "edit":
                            for b in game._menu.mem_tamp["list_bat"]["add"]["bat"]:
                                game._map.add_build(b)
                            for b in game._menu.mem_tamp["list_bat"]["sup"]:
                                game._map.sup_build(b)
                        game._menu.set_action("edit")
                    if button[0] == "edit_annulation":
                        game._menu.mem_tamp = None
                        game._menu.set_action("edit")
                    if button[0] == "edit_construction":
                        game._menu.set_action("edit-add")
                    if button[0] == "edit_destruction":
                        game._menu.set_action("edit-sup")
        elif event.type == pygame.KEYUP: #lors de l'appui d'une touche
            if k[pygame.K_F1]:
                game._menu.set_action("settings")
            if k[pygame.K_r]:
                game._menu.set_action("ressources")
            if k[pygame.K_e]:
                game._menu.set_action("edit")
            if game._menu.mem_tamp is not None and game._menu.mem_tamp["bat"] is not None:
                if k[pygame.K_UP]:
                    game._menu.mem_tamp["bat"]["angle"] = 90
                if k[pygame.K_RIGHT]:
                    game._menu.mem_tamp["bat"]["angle"] = 0
                if k[pygame.K_DOWN]:
                    game._menu.mem_tamp["bat"]["angle"] = 270
                if k[pygame.K_LEFT]:
                    game._menu.mem_tamp["bat"]["angle"] = 180
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                continuer = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            continuer = False