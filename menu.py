from tools import *
from buttons import Button
from buildings import DICT_BUILDINGS

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
        pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0], cst("POS_Y_BOTTOM_MENU_EDIT")), (cst("size_x"), cst("POS_Y_BOTTOM_MENU_EDIT")))
        for b in self.mem_tamp["list_bat"]["add"]["bat"]:
            b.display(screen, *pos_map)

    def display_ressources(self, screen, ressources : dict): #à faire : créer les constantes au début pour éviter les calculs
        """
        fonction permettant d'afficher les ressources
        """
        screen.fill(cst("BLACK"))
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(cst("size_x")//4, cst("size_y")//4, cst("size_x")//2, cst("size_y")//2), 0)
        ressources = list(ressources.items())
        for i in range(len(ressources)):
            res = ressources[i]
            ratio = res[1][1] / res[1][0]
            t.barre(screen, (cst("size_x")/2-cst("size_x")/16, cst("size_y")*(3*len(ressources)+2+6*i)/(12*len(ressources))), (cst("size_x")/8, cst("size_y")/(6*len(ressources))), ratio, cst("RED"))
            t.text(screen, res[0], cst("BLACK"), (cst("size_x")/4+cst("size_x")/16, cst("size_y")/4+cst("size_y")/(6*len(ressources))+i*cst("size_y")/(2*len(ressources))), int(cst("size_y")/(6*len(ressources))))
            t.text(screen, str(res[1][1])+"/"+str(res[1][0])+" ("+str(round(ratio*100, 2))+"%)", cst("BLACK"), (cst("size_x")/2+cst("size_x")/8, cst("size_y")/4+cst("size_y")/(6*len(ressources))+i*cst("size_y")/(2*len(ressources))), int(cst("size_y")/(6*len(ressources))))

    def display_settings(self, screen):
        """
        fonction permettant d'afficher les paramètres du jeu
        """
        screen.fill(cst("BLACK"))
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(cst("size_x")//4, cst("size_y")//4, cst("size_x")//2, cst("size_y")//2), 0)
    
    def click(self, pos, _map):
        if self.action.startswith("edit"): #si un edit est en cours
            if self.mem_tamp is not None and (not cst("MENU_EDIT_POS")[0] < pos[0] or not cst("MENU_EDIT_POS")[1] < pos[1]): #si le clic est sur la map
                place_x, place_y = t.get_case(pos, _map) #récupération des cases
                if self.action == "edit-add" and self.mem_tamp["bat"] is not None: #si un bâtiment à construire est séléctionné
                    #construction bâtiment
                    build = DICT_BUILDINGS[self.mem_tamp["bat"]["bat"]](place_x, place_y) #on instancie le bâtiment
                    build.rotate(self.mem_tamp["bat"]["angle"])
                    place = _map.check_pos(build, self.mem_tamp["list_bat"]["add"]["pos"])
                    if place == 0: #on vérifie que la place est libre
                        self.mem_tamp["list_bat"]["add"]["bat"].append(build) #on ajoute le bâtiment dans la mémoire tampon
                        for x in range(build.pos[0], build.pos[0]+build.size[0]):
                            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                self.mem_tamp["list_bat"]["add"]["pos"].append((x, y))
                    elif place == 2: #annuler la construction d'un batiment
                        for b in self.mem_tamp["list_bat"]["add"]["bat"]:
                            for x in range(b.pos[0], b.pos[0]+b.size[0]):
                                for y in range(b.pos[1], b.pos[1]+b.size[1]):
                                    if (place_x, place_y) == (x, y):
                                        build = b
                        for x in range(build.pos[0], build.pos[0]+build.size[0]):
                            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                self.mem_tamp["list_bat"]["add"]["pos"].remove((x, y))
                        self.mem_tamp["list_bat"]["add"]["bat"].remove(build)
                    else:
                        del build
                elif self.action == "edit-sup":
                    #destruction d'un bâtiment
                    build = None
                    for b in _map.list_build:
                        for x in range(b.pos[0], b.pos[0]+b.size[0]):
                            for y in range(b.pos[1], b.pos[1]+b.size[1]):
                                if (place_x, place_y) == (x, y):
                                    build = b
                    if build is not None:
                        self.mem_tamp["list_bat"]["sup"].append(build)
            #sélection bâtiment
            elif cst("MENU_EDIT_POS")[0] < pos[0] and cst("MENU_EDIT_POS")[1] < pos[1] < cst("POS_Y_BOTTOM_MENU_EDIT") : #si le clic est dans le menu d'edition
                if self.action == "edit-add":
                    pos[0], pos[1] = pos[0] - cst("MENU_EDIT_POS")[0], pos[1] - cst("MENU_EDIT_POS")[1]
                    coord_case = (int(pos[0]/cst("LONG_COL_MENU_EDIT")), int(pos[1]/cst("LONG_COL_MENU_EDIT"))) #on calcul les coordonnées de la case
                    index = 3*coord_case[1] + coord_case[0] #on calcul l'index de la case dans la liste des bâtiments
                    self.mem_tamp["bat"] = {"bat" : cst("LIST_BAT_MENU_EDIT")[index], "angle" : 0} #on ajoute le bâtiment à la mémoire tampon dans la section réservé au bâtiment séléctinné pour de la construction
        for button in self.buttons.items():
            if button[1].collidepoint(pos):
                if button[0] == "edit_validation":
                    if self.action == "edit":
                        for b in self.mem_tamp["list_bat"]["add"]["bat"]:
                            _map.add_build(b)
                        for b in self.mem_tamp["list_bat"]["sup"]:
                            _map.sup_build(b)
                    self.set_action("edit")
                if button[0] == "edit_annulation":
                    self.mem_tamp = None
                    self.set_action("edit")
                if button[0] == "edit_construction":
                    self.set_action("edit-add")
                if button[0] == "edit_destruction":
                    self.set_action("edit-sup")