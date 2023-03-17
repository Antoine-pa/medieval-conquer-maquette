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
        print("ok")

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
        if self.action == "edit-add":
            self.buttons["edit_angle"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), str(int(4*self.mem_tamp["bat"]["angle"]/360)), 1)
            self.buttons["edit_annulation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT")+cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "n", 1)
            self.buttons["edit_validation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+2*cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT")+2*cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "y", 1)
        elif self.action == "edit":
            self.buttons["edit_construction"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "c", 1)
            self.buttons["edit_destruction"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT")+cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "d", 1)
            self.buttons["edit_validation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+2*cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT")+2*cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "y", 1)
        elif self.action == "edit-sup":
            self.buttons["edit_annulation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT"), cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "n", 1)
            self.buttons["edit_validation"] = Button((cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1], cst("MENU_EDIT_POS")[0]+cst("POS_BUTTONS_MENU_EDIT")[0]+cst("LONG_BLOCK_MENU_EDIT")+cst("MENU_EDIT_POS")[3], cst("POS_BUTTONS_MENU_EDIT")[1]+cst("LONG_BLOCK_MENU_EDIT")), "y", 1)


    def update_mem_tamp(self):
        if self.action.startswith("edit"):
            self.mem_tamp = {"bat" : {"bat" : None, "angle" : 0}, "list_bat" : {"add" : {"pos" : [], "bat" : []}, "sup" : []}, "ress" : {"bois" : 2, "fer" : 6}}
        else:
            self.mem_tamp = None


    def display(self, screen, ressources : dict, pos_map: list):
        """
        fonction permettant d'afficher les zones des sections du menu
        """
        if self.action == "map":
            pass
        elif self.action.startswith("edit"):
            self.display_edit(screen, pos_map, ressources)
        elif self.action == "settings":
            self.display_settings(screen)
        elif self.action == "ressources":
            self.display_ressources(screen, ressources)
        for button in self.buttons.items():
            button[1].display(screen)

    def display_edit(self, screen, pos_map: list, ressources):
        """
        fonction permettant d'afficher le menu d'edition de la map
        """
        #display all buildings in mem tamp
        for b in self.mem_tamp["list_bat"]["add"]["bat"]:
            d = b.display(screen, *pos_map)
            if d: #si le bâtiment est affiché
                pygame.draw.rect(screen, cst("GREY_YELLOW"), pygame.Rect((b.pos[0] - pos_map[0])*cst("SIZE_CASE"), (b.pos[1] - pos_map[1])*cst("SIZE_CASE"), cst("SIZE_CASE")*b.size[0], cst("SIZE_CASE")*b.size[1]), 3)

        for b in self.mem_tamp["list_bat"]["sup"]:
            if b.in_windows(*pos_map):
                pygame.draw.rect(screen, cst("RED_ORANGE"), pygame.Rect((b.pos[0] - pos_map[0])*cst("SIZE_CASE"), (b.pos[1] - pos_map[1])*cst("SIZE_CASE"), cst("SIZE_CASE")*b.size[0], cst("SIZE_CASE")*b.size[1]), 3)

        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(*cst("MENU_EDIT_POS")), 0)
        if self.action == "edit-add":
            pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(max(0, cst("MENU_EDIT_POS")[0] - len(cst("LIST_BAT_MENU_EDIT"))*cst("MENU_EDIT_POS")[3]), cst("MENU_EDIT_POS")[1], cst("size_x")-cst("MENU_EDIT_POS")[2], cst("MENU_EDIT_POS")[3])) #rectangle des bâtiments suplémentaires
            pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[:2]), (cst("MENU_EDIT_POS")[0], cst("size_y")), 3) #ligne entre les bouttons et les bâtiments
            ress = self.mem_tamp["ress"]
            pos_menu = (cst("size_x") - 4*cst("MENU_EDIT_POS")[3], cst("size_y") - (len(ress)+1)*cst("MENU_EDIT_POS")[3], 4*cst("MENU_EDIT_POS")[3], len(ress)*cst("MENU_EDIT_POS")[3])
            for i in range(len(cst("LIST_BAT_MENU_EDIT"))):
                build = cst("LIST_BAT_MENU_EDIT")[i]
                if self.mem_tamp["bat"]["bat"] == build:
                    pygame.draw.rect(screen, cst("GREY_YELLOW"), pygame.Rect((cst("MENU_EDIT_POS")[0] - (i+1)*(cst("MENU_EDIT_POS")[3]), cst("MENU_EDIT_POS")[1]), (cst("MENU_EDIT_POS")[3], cst("MENU_EDIT_POS")[3]))) #si le bâtiment est sélectionné, on color en jaune en dessous
                    cost = t.cost(build, 1)
                    pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(pos_menu[0] - pos_menu[2], cst("MENU_EDIT_POS")[1] - len(cost) * (cst("MENU_EDIT_POS")[3]), pos_menu[2], len(cost) * (cst("MENU_EDIT_POS")[3])))
                    cost = list(cost.items())
                    pygame.draw.line(screen, cst("BLACK"), (pos_menu[0]-1, cst("MENU_EDIT_POS")[1] - len(cost) * (cst("MENU_EDIT_POS")[3])), (pos_menu[0]-1, cst("MENU_EDIT_POS")[1]), 1)
                    for j in range(len(cost)):
                        res = cost[j]
                        t.text(screen, res[0] + " : " + str(res[1]), cst("BLACK"), (pos_menu[0] - pos_menu[2] + cst("MENU_EDIT_POS")[3] // 4, cst("MENU_EDIT_POS")[1] - len(cost) * (cst("MENU_EDIT_POS")[3]) + j * cst("MENU_EDIT_POS")[3] + cst("MENU_EDIT_POS")[3] // 4), 20)
                img = t.load_img("./assets/buildings/"+build+".png", cst("LONG_BLOCK_MENU_EDIT"), cst("LONG_BLOCK_MENU_EDIT")) #on charge l'image
                pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0] - (i+1)*cst("MENU_EDIT_POS")[3], cst("MENU_EDIT_POS")[1]), (cst("MENU_EDIT_POS")[0] - (i+1)*cst("MENU_EDIT_POS")[3], cst("size_y"))) #on met une ligne entre les bâtiments
                screen.blit(img, (cst("MENU_EDIT_POS")[0] - (i+1)*cst("MENU_EDIT_POS")[3] + cst("GAP_BLOCK_COL_MENU_EDIT"), cst("MENU_EDIT_POS")[1] + cst("GAP_BLOCK_COL_MENU_EDIT"))) #on affiche l'image
            pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0] - (i + 1) * (cst("MENU_EDIT_POS")[3]), cst("size_y") - cst("MENU_EDIT_POS")[3]), (cst("size_x"), cst("size_y") - cst("MENU_EDIT_POS")[3])) #on rajoute une ligne au dessus
            if pos_menu[3] != 0: #si des ressources sont utilisées
                pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(*pos_menu), 0)  # on ajoute le rectangle supérieur
                ress = list(ress.items())
                for i in range(len(ress)):
                    res = ress[i]
                    t.text(screen, res[0]+" : "+str(res[1])+"/"+str(ressources[res[0]][0]), cst("BLACK"), (pos_menu[0]+cst("MENU_EDIT_POS")[3]//4, pos_menu[1]+i*cst("MENU_EDIT_POS")[3]+cst("MENU_EDIT_POS")[3]//4), 20) #on ajoute la ligne de ressource


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
        if self.action == "edit-add": #si il ajoute des bâtiments
            pos_menu = (max(0, cst("MENU_EDIT_POS")[0] - len(cst("LIST_BAT_MENU_EDIT"))*cst("MENU_EDIT_POS")[3]), cst("MENU_EDIT_POS")[1])
            if pos_menu[0] < pos[0] and pos_menu[1] < pos[1]: #si le clic est dans le menu d'edition
                if pos[0] < cst("MENU_EDIT_POS")[0]: #si il click dans les bâtiments et non dans les bouttons
                    #sélection bâtiment
                    pos[0], pos[1] = pos[0] - pos_menu[0], pos[1] - pos_menu[1]
                    coord_case = int(pos[0]/cst("MENU_EDIT_POS")[3]) #on calcul les coordonnées de la case
                    index = len(cst("LIST_BAT_MENU_EDIT")) - coord_case - 1 #on calcul l'index de la case dans la liste des bâtiments
                    if self.mem_tamp["bat"]["bat"] != cst("LIST_BAT_MENU_EDIT")[index]:
                        self.mem_tamp["bat"]["bat"] = cst("LIST_BAT_MENU_EDIT")[index] #on ajoute le bâtiment à la mémoire tampon dans la section réservé au bâtiment séléctinné pour de la construction
                    else:
                        self.mem_tamp["bat"]["bat"] = None
            else: #si le clic est sur la map
                place_x, place_y = t.get_case(pos, _map) #récupération des cases
                if self.mem_tamp["bat"]["bat"] is not None: #si un bâtiment à construire est séléctionné
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
                                        del build
                                        build = b
                        for x in range(build.pos[0], build.pos[0]+build.size[0]):
                            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                self.mem_tamp["list_bat"]["add"]["pos"].remove((x, y))
                        self.mem_tamp["list_bat"]["add"]["bat"].remove(build)
                        del build
                    else:
                        del build
        elif self.action == "edit-sup":
            #destruction d'un bâtiment
            place_x, place_y = t.get_case(pos, _map) #récupération des cases
            build = None
            for b in _map.list_build:
                for x in range(b.pos[0], b.pos[0]+b.size[0]):
                    for y in range(b.pos[1], b.pos[1]+b.size[1]):
                        if (place_x, place_y) == (x, y):
                            build = b
            if build is not None:
                if build in self.mem_tamp["list_bat"]["sup"]:
                    self.mem_tamp["list_bat"]["sup"].remove(build)
                else:
                    self.mem_tamp["list_bat"]["sup"].append(build)
        for button in self.buttons.items():
            if button[1].collidepoint(pos):
                if button[0] == "edit_validation":
                    if self.action.startswith("edit"):
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