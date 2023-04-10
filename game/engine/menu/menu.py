from engine import cst, Button, t, DICT_BUILDINGS
import pygame

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

    def set_action(self, act : str, _map):
        """
        fonction permettant de changer de section du menu
        """
        if self.action != act:
            self.action = act
        else:
            self.action = "map"
        self.update_mem_tamp()
        self.update_buttons(_map)

    def update_buttons(self, _map):
        self.buttons = {}
        self.buttons["change_layer"] = Button((50, 50, 150, 100), "layer", 1)
        if _map.layer == -1:
            self.buttons["change_transparency"] = Button((50, 150, 150, 200), "trans", 1)
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
            self.mem_tamp = {"bat": {"bat": None, "angle": 0}, "list_bat": {0 : {"add": {"pos": [], "bat": []}, "sup": []}, -1 : {"add": {"pos": [], "bat": []}, "sup": []}}, "ress": {}}
        else:
            self.mem_tamp = None


    def display(self, screen, _map):
        """
        fonction permettant d'afficher les zones des sections du menu
        """
        if self.action == "map":
            pass
        elif self.action.startswith("edit"):
            self.display_edit(screen, _map)
        elif self.action == "settings":
            self.display_settings(screen)
        elif self.action == "ressources":
            self.display_ressources(screen)
        for button in self.buttons.values():
            button.display(screen)

    def display_edit(self, screen, _map):
        """
        fonction permettant d'afficher le menu d'edition de la map
        """
        #display all buildings in mem tamp
        for b in self.mem_tamp["list_bat"][_map.layer]["add"]["bat"]:
            d = b.display(screen, *_map.pos)
            if d: #si le bâtiment est affiché
                pygame.draw.rect(screen, cst("GREY_YELLOW"), pygame.Rect((b.pos[0] - _map.pos[0])*int(cst("SIZE_CASE")), (b.pos[1] - _map.pos[1])*int(cst("SIZE_CASE")), int(cst("SIZE_CASE"))*b.size[0], int(cst("SIZE_CASE"))*b.size[1]), 3)

        for b in self.mem_tamp["list_bat"][_map.layer]["sup"]:
            if b.in_windows(*_map.pos):
                pygame.draw.rect(screen, cst("RED_ORANGE"), pygame.Rect((b.pos[0] - _map.pos[0])*int(cst("SIZE_CASE")), (b.pos[1] - _map.pos[1])*int(cst("SIZE_CASE")), int(cst("SIZE_CASE"))*b.size[0], int(cst("SIZE_CASE"))*b.size[1]), 3)

        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(*cst("MENU_EDIT_POS")), 0)
        if self.action == "edit-add":
            pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(max(0, cst("MENU_EDIT_POS")[0] - len(cst("LIST_BAT_MENU_EDIT")[str(_map.layer)])*cst("MENU_EDIT_POS")[3]), cst("MENU_EDIT_POS")[1], cst("size_x")-cst("MENU_EDIT_POS")[2], cst("MENU_EDIT_POS")[3])) #rectangle des bâtiments suplémentaires
            pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[:2]), (cst("MENU_EDIT_POS")[0], cst("size_y")), 3) #ligne entre les bouttons et les bâtiments
            ress = self.mem_tamp["ress"]
            pos_menu = (cst("size_x") - 4*cst("MENU_EDIT_POS")[3], cst("size_y") - (len(ress)+1)*cst("MENU_EDIT_POS")[3], 4*cst("MENU_EDIT_POS")[3], len(ress)*cst("MENU_EDIT_POS")[3])
            check = None
            for i in range(len(cst("LIST_BAT_MENU_EDIT")[str(_map.layer)])):
                build = cst("LIST_BAT_MENU_EDIT")[str(_map.layer)][i]
                if self.mem_tamp["bat"]["bat"] == build:
                    pygame.draw.rect(screen, cst("GREY_YELLOW"), pygame.Rect((cst("MENU_EDIT_POS")[0] - (i+1)*(cst("MENU_EDIT_POS")[3]), cst("MENU_EDIT_POS")[1]), (cst("MENU_EDIT_POS")[3], cst("MENU_EDIT_POS")[3]))) #si le bâtiment est sélectionné, on color en jaune en dessous
                    cost = t.cost(build, 1)
                    pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(pos_menu[0] - pos_menu[2], cst("MENU_EDIT_POS")[1] - len(cost) * (cst("MENU_EDIT_POS")[3]), pos_menu[2], len(cost) * (cst("MENU_EDIT_POS")[3])))
                    cost = list(cost.items())
                    pygame.draw.line(screen, cst("BLACK"), (pos_menu[0]-1, cst("MENU_EDIT_POS")[1] - len(cost) * (cst("MENU_EDIT_POS")[3])), (pos_menu[0]-1, cst("MENU_EDIT_POS")[1]), 1)
                    check = t.check_res(t.cost(build, 1), self.mem_tamp["ress"])
                    for j in range(len(cost)):
                        res = cost[j]
                        if check == res[0]:
                            color = cst("RED")
                        else:
                            color = cst("BLACK")
                        t.text(screen, res[0] + " : " + str(res[1]), color, (pos_menu[0] - pos_menu[2] + cst("MENU_EDIT_POS")[3] // 4, cst("MENU_EDIT_POS")[1] - len(cost) * (cst("MENU_EDIT_POS")[3]) + j * cst("MENU_EDIT_POS")[3] + cst("MENU_EDIT_POS")[3] // 4), 20)
                b = build
                if build == "Wall":
                    build += "2_0"
                img = t.load_img("buildings/"+b+"/"+build+".png", cst("LONG_BLOCK_MENU_EDIT"), cst("LONG_BLOCK_MENU_EDIT")) #on charge l'image
                pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0] - (i+1)*cst("MENU_EDIT_POS")[3], cst("MENU_EDIT_POS")[1]), (cst("MENU_EDIT_POS")[0] - (i+1)*cst("MENU_EDIT_POS")[3], cst("size_y"))) #on met une ligne entre les bâtiments
                screen.blit(img, (cst("MENU_EDIT_POS")[0] - (i+1)*cst("MENU_EDIT_POS")[3] + cst("GAP_BLOCK_COL_MENU_EDIT"), cst("MENU_EDIT_POS")[1] + cst("GAP_BLOCK_COL_MENU_EDIT"))) #on affiche l'image
            pygame.draw.line(screen, cst("BLACK"), (cst("MENU_EDIT_POS")[0] - (i + 1) * (cst("MENU_EDIT_POS")[3]), cst("size_y") - cst("MENU_EDIT_POS")[3]), (cst("size_x"), cst("size_y") - cst("MENU_EDIT_POS")[3])) #on rajoute une ligne au dessus
            if pos_menu[3] != 0: #si des ressources sont utilisées
                pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(*pos_menu), 0)  # on ajoute le rectangle supérieur
                ress = list(ress.items())
                for i in range(len(ress)):
                    res = ress[i]
                    if check is not None and check == res[0]:
                        color = cst("RED")
                    else:
                        color = cst("BLACK")
                    t.text(screen, res[0]+" : "+str(res[1])+"/"+str(t.res(res[0])["stock"]), color, (pos_menu[0]+cst("MENU_EDIT_POS")[3]//4, pos_menu[1]+i*cst("MENU_EDIT_POS")[3]+cst("MENU_EDIT_POS")[3]//4), 20) #on ajoute la ligne de ressource


    def display_ressources(self, screen): #à faire : créer les constantes au début pour éviter les calculs
        """
        fonction permettant d'afficher les ressources
        """
        resources = t.data_res
        screen.fill(cst("BLACK"))
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(cst("size_x")//4, cst("size_y")//4, cst("size_x")//2, cst("size_y")//2), 0)
        resources = list(resources.items())
        for i in range(len(resources)):
            res = resources[i]
            ratio = res[1]["stock"] / res[1]["max"]
            t.barre(screen, (cst("size_x")/2-cst("size_x")/16, cst("size_y")*(3*len(resources)+2+6*i)/(12*len(resources))), (cst("size_x")/8, cst("size_y")/(6*len(resources))), ratio, cst("RED"))
            t.text(screen, res[0], cst("BLACK"), (cst("size_x")/4+cst("size_x")/16, cst("size_y")/4+cst("size_y")/(6*len(resources))+i*cst("size_y")/(2*len(resources))), int(cst("size_y")/(6*len(resources))))
            t.text(screen, str(res[1]["stock"])+"/"+str(res[1]["max"])+" ("+str(round(ratio*100, 2))+"%)", cst("BLACK"), (cst("size_x")/2+cst("size_x")/8, cst("size_y")/4+cst("size_y")/(6*len(resources))+i*cst("size_y")/(2*len(resources))), int(cst("size_y")/(6*len(resources))))

    def display_settings(self, screen):
        """
        fonction permettant d'afficher les paramètres du jeu
        """
        screen.fill(cst("BLACK"))
        pygame.draw.rect(screen, cst("GREY_WHITE"), pygame.Rect(cst("size_x")//4, cst("size_y")//4, cst("size_x")//2, cst("size_y")//2), 0)

    def click(self, pos, _map):
        if self.action == "edit-add": #si il ajoute des bâtiments
            pos_menu = (max(0, cst("MENU_EDIT_POS")[0] - len(cst("LIST_BAT_MENU_EDIT")[str(_map.layer)])*cst("MENU_EDIT_POS")[3]), cst("MENU_EDIT_POS")[1])
            if pos_menu[0] < pos[0] and pos_menu[1] < pos[1]: #si le clic est dans le menu d'edition
                if pos[0] < cst("MENU_EDIT_POS")[0]: #si il click dans les bâtiments et non dans les bouttons
                    #sélection bâtiment
                    pos[0], pos[1] = pos[0] - pos_menu[0], pos[1] - pos_menu[1]
                    coord_case = int(pos[0]/cst("MENU_EDIT_POS")[3]) #on calcul les coordonnées de la case
                    index = len(cst("LIST_BAT_MENU_EDIT")[str(_map.layer)]) - coord_case - 1 #on calcul l'index de la case dans la liste des bâtiments
                    if self.mem_tamp["bat"]["bat"] != cst("LIST_BAT_MENU_EDIT")[str(_map.layer)][index]:
                        self.mem_tamp["bat"]["bat"] = cst("LIST_BAT_MENU_EDIT")[str(_map.layer)][index] #on ajoute le bâtiment à la mémoire tampon dans la section réservé au bâtiment séléctinné pour de la construction
                    else:
                        self.mem_tamp["bat"]["bat"] = None
            else: #si le clic est sur la map
                place_x, place_y = t.get_case(pos, _map) #récupération des cases
                if self.mem_tamp["bat"]["bat"] is not None: #si un bâtiment à construire est séléctionné
                    #construction bâtiment
                    build = DICT_BUILDINGS[self.mem_tamp["bat"]["bat"]]([place_x, place_y]) #on instancie le bâtiment
                    build.rotate(self.mem_tamp["bat"]["angle"])
                    place = _map.check_pos(build, self.mem_tamp["list_bat"][_map.layer]["add"]["pos"])
                    if place == 0 and t.check_res(t.cost(build.name, 1), self.mem_tamp["ress"]) == True: #on vérifie que la place est libre et que les ressources sont suffisantes
                        self.mem_tamp["list_bat"][_map.layer]["add"]["bat"].append(build) #on ajoute le bâtiment dans la mémoire tampon
                        for x in range(build.pos[0], build.pos[0]+build.size[0]):
                            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                self.mem_tamp["list_bat"][_map.layer]["add"]["pos"].append((x, y))
                        for ress in t.cost(build.name, 1).items():
                            if ress[0] not in self.mem_tamp["ress"]:
                                self.mem_tamp["ress"][ress[0]] = 0
                            self.mem_tamp["ress"][ress[0]] += ress[1]
                        if build.name == "Wall":
                            builds_changing = []
                            for b in self.mem_tamp["list_bat"][_map.layer]["add"]["bat"] + _map.dict_name_build[_map.layer].get("Wall", []):
                                if b.name == "Wall" and b != build and ((abs(b.pos[0] - build.pos[0]) == 1 and abs(b.pos[1] - build.pos[1]) == 0) or (abs(b.pos[0] - build.pos[0]) == 0 and abs(b.pos[1] - build.pos[1]) == 1)):
                                    if b.pos[0] == build.pos[0] and b.pos[1] < build.pos[1]: #positionnement en bas d'une autre muraille
                                        build.t[1] = 1
                                        b.t[3] = 1
                                    elif b.pos[0] == build.pos[0] and b.pos[1] > build.pos[1]: #positionnement en haut d'une autre muraille
                                        build.t[3] = 1
                                        b.t[1] = 1
                                    elif b.pos[0] > build.pos[0] and b.pos[1] == build.pos[1]: #positionnement à gauche d'une autre muraille
                                        build.t[0] = 1
                                        b.t[2] = 1
                                    elif b.pos[0] < build.pos[0] and b.pos[1]  == build.pos[1]: #positionnement à droite d'une autre muraille
                                        build.t[2] = 1
                                        b.t[0] = 1
                                    builds_changing.append(b)
                            builds_changing.append(build)
                            t.rotate_wall(builds_changing)
                    elif place == 2: #annuler la construction d'un batiment
                        for b in self.mem_tamp["list_bat"][_map.layer]["add"]["bat"]:
                            for x in range(b.pos[0], b.pos[0]+b.size[0]):
                                for y in range(b.pos[1], b.pos[1]+b.size[1]):
                                    if (place_x, place_y) == (x, y):
                                        del build
                                        build = b
                        if build.name == "Wall":
                            builds_changing = []
                            for b in self.mem_tamp["list_bat"][_map.layer]["add"]["bat"] + _map.dict_name_build[_map.layer].get("Wall", []):
                                if b.name == "Wall" and ((abs(b.pos[0] - build.pos[0]) == 1 and abs(b.pos[1] - build.pos[1]) == 0) or (abs(b.pos[0] - build.pos[0]) == 0 and abs(b.pos[1] - build.pos[1]) == 1)):
                                    if b.pos[0] == build.pos[0] and b.pos[1]  < build.pos[1]: #positionnement en bas d'une autre muraille
                                        b.t[3] = 0
                                    elif b.pos[0] == build.pos[0] and b.pos[1]  > build.pos[1]: #positionnement en haut d'une autre muraille
                                        b.t[1] = 0
                                    elif b.pos[0] > build.pos[0] and b.pos[1]  == build.pos[1]: #positionnement à gauche d'une autre muraille
                                        b.t[2] = 0
                                    elif b.pos[0] < build.pos[0] and b.pos[1]  == build.pos[1]: #positionnement à droite d'une autre muraille
                                        b.t[0] = 0
                                    builds_changing.append(b)
                            t.rotate_wall(builds_changing)
                        for ress in t.cost(build.name, 1).items():
                            self.mem_tamp["ress"][ress[0]] -= ress[1]
                            if self.mem_tamp["ress"][ress[0]] == 0:
                                del self.mem_tamp["ress"][ress[0]]
                        for x in range(build.pos[0], build.pos[0]+build.size[0]):
                            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                                self.mem_tamp["list_bat"][_map.layer]["add"]["pos"].remove((x, y))
                        self.mem_tamp["list_bat"][_map.layer]["add"]["bat"].remove(build)
                        del build
                    else:
                        del build
        elif self.action == "edit-sup":
            #destruction d'un bâtiment
            place_x, place_y = t.get_case(pos, _map) #récupération des cases
            build = _map.dict_pos_build[_map.layer].get((place_x, place_y))
            if build is not None:
                if build in self.mem_tamp["list_bat"][_map.layer]["sup"]:
                    self.mem_tamp["list_bat"][_map.layer]["sup"].remove(build)
                else:
                    self.mem_tamp["list_bat"][_map.layer]["sup"].append(build)
        for button in self.buttons.items():
            if button[1].collidepoint(pos):
                if button[0] == "edit_validation":
                    if self.action.startswith("edit"):
                        for build in self.mem_tamp["list_bat"][_map.layer]["add"]["bat"]:
                            _map.add_build(build)
                        for build in self.mem_tamp["list_bat"][_map.layer]["sup"]:
                            if build.name == "Wall":
                                builds_changing = []
                                for b in _map.dict_name_build[_map.layer].get("Wall", []):
                                    if b.name == "Wall" and ((abs(b.pos[0] - build.pos[0]) == 1 and abs(b.pos[1] - build.pos[1]) == 0) or (abs(b.pos[0] - build.pos[0]) == 0 and abs(b.pos[1] - build.pos[1]) == 1)):
                                        if b.pos[0] == build.pos[0] and b.pos[1]  < build.pos[1]: #positionnement en bas d'une autre muraille
                                            b.t[3] = 0
                                        elif b.pos[0] == build.pos[0] and b.pos[1]  > build.pos[1]: #positionnement en haut d'une autre muraille
                                            b.t[1] = 0
                                        elif b.pos[0] > build.pos[0] and b.pos[1]  == build.pos[1]: #positionnement à gauche d'une autre muraille
                                            b.t[2] = 0
                                        elif b.pos[0] < build.pos[0] and b.pos[1]  == build.pos[1]: #positionnement à droite d'une autre muraille
                                            b.t[0] = 0
                                        builds_changing.append(b)
                                t.rotate_wall(builds_changing)
                            _map.sup_build(build)
                        for r in self.mem_tamp["ress"].items():
                            t.set_res(r[0], t.res(r[0])["stock"] - r[1])
                        t.save_map(_map)
                    self.set_action("edit", _map)
                if button[0] in ("edit_annulation", "change_layer"):
                    self.mem_tamp = None
                    self.set_action("edit", _map)
                if button[0] == "edit_construction":
                    self.set_action("edit-add", _map)
                if button[0] == "edit_destruction":
                    self.set_action("edit-sup", _map)
                if button[0] == "change_layer":
                    if _map.layer == 0:
                        _map.layer = -1
                    else:
                        _map.layer = 0
                    self.update_buttons(_map)
                if button[0] == "change_transparency":
                    _map.alpha = not _map.alpha