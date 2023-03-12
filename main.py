import pygame
import time

pygame.init()
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w,screen_info.current_h))
size_x = screen_info.current_w
size_y = screen_info.current_h


BLACK = (0, 0, 0)
RED = (150, 0, 0)
WHITE = (255, 255, 255)
GREY_WHITE = (200, 200, 200)
GREY = (100, 100, 100)
SENSIBILITY = 0.4
MENU_EDIT_POS = (5*size_x//6, size_y//2, size_x//6, size_y//2)
LONG_COL_MENU_EDIT = MENU_EDIT_POS[2] // 3
LONG_BLOCK_MENU_EDIT = 2*LONG_COL_MENU_EDIT//3
GAP_BLOCK_COL_MENU_EDIT = LONG_COL_MENU_EDIT//6
LIST_BAT_MENU_EDIT = ["Caserne", "Champs", "Grenier"]
ZOOM = 1
SIZE_CASE_INIT = 50
SIZE_CASE = SIZE_CASE_INIT


def load_img(name, x, y):
    img = pygame.image.load(name)
    img = pygame.transform.scale(img,(x, y))
    return img


class Map:
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.pos = [self.x/2, self.y/2]
        self.list_build = []
        self.cases = []
        self.add_build(Caserne(503, 506))
        

    def display(self):
        screen.fill(WHITE)
        for x in range(0, size_x+int(SIZE_CASE), int(SIZE_CASE)):
            pygame.draw.line(screen, BLACK, (x-self.pos[0]%1*int(SIZE_CASE), 0), (x-self.pos[0]%1*int(SIZE_CASE), size_y))
            for y in range(0, size_y+int(SIZE_CASE), int(SIZE_CASE)):
                pygame.draw.line(screen, BLACK, (0, y-self.pos[1]%1*int(SIZE_CASE)), (size_x, y-self.pos[1]%1*int(SIZE_CASE)))
        for b in self.list_build:
            b.display(*self.pos)
    
    def add_build(self, build):
        self.list_build.append(build)
        for x in range(build.pos[0], build.pos[0]+build.size[0]):
            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                self.cases.append((x, y))
    
    def check_pos(self, build):
        for x in range(build.pos[0], build.pos[0]+build.size[0]):
            for y in range(build.pos[1], build.pos[1]+build.size[1]):
                if (x, y) in self.cases:
                    return False
        return True
    
    def reload_images(self):
        for b in self.list_build:
            b.load()

class Menu:
    def __init__(self):
        self.action = "map"
        self.mem_tamp = None

    def click(self, act):
        if self.action != act:
            if act == "edit":
                self.mem_tamp = [None, None, None]
            else:
                self.mem_tamp = None
            self.action = act
        else:
            self.action = "map"
            self.mem_tamp = None


    def display(self, screen, ressources):
        if self.action == "map":
            pass
        elif self.action == "edit":
            pygame.draw.rect(screen, GREY_WHITE, pygame.Rect(*MENU_EDIT_POS), 0)
            for i in range(len(LIST_BAT_MENU_EDIT)):
                img = load_img("./assets/buildings/"+LIST_BAT_MENU_EDIT[i]+".png", LONG_BLOCK_MENU_EDIT, LONG_BLOCK_MENU_EDIT)
                pygame.draw.line(screen, BLACK, (MENU_EDIT_POS[0] + (i+1)*LONG_COL_MENU_EDIT, MENU_EDIT_POS[1]), (MENU_EDIT_POS[0]+ (i+1)*LONG_COL_MENU_EDIT, size_y))
                screen.blit(img, (MENU_EDIT_POS[0] + i*LONG_COL_MENU_EDIT + GAP_BLOCK_COL_MENU_EDIT, MENU_EDIT_POS[1] + GAP_BLOCK_COL_MENU_EDIT))
        elif self.action == "settings":
            self.display_settings(screen)
        elif self.action == "ressources":
            self.display_ressources(screen, ressources)


    def display_ressources(self, screen, ressources):
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY_WHITE, pygame.Rect(size_x//4, size_y//4, size_x//2, size_y//2), 0)
        ressources = list(ressources.items())
        for i in range(len(ressources)):
            res = ressources[i]
            ratio = res[1][1] / res[1][0]
            barre((size_x/2-size_x/16, size_y*(3*len(ressources)+2+6*i)/(12*len(ressources))), (size_x/8, size_y/(6*len(ressources))), ratio, RED)
            Text(res[0], BLACK, (size_x/4+size_x/16, size_y/4+size_y/(6*len(ressources))+i*size_y/(2*len(ressources))), int(size_y/(6*len(ressources))))
            Text(str(res[1][1])+"/"+str(res[1][0])+" ("+str(round(ratio*100, 2))+"%)", BLACK, (size_x/2+size_x/8, size_y/4+size_y/(6*len(ressources))+i*size_y/(2*len(ressources))), int(size_y/(6*len(ressources))))

    def display_settings(self, screen):
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY_WHITE, pygame.Rect(size_x//4, size_y//4, size_x//2, size_y//2), 0)

def barre(pos : tuple, size : tuple, ratio : float, color : tuple):
    pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], size[0]*ratio, size[1]), 0)
    pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], size[0], size[1]), 1)


def Text(text, color, pos: tuple, size):
    """
    fonction pour afficher du text
    """
    FONT = pygame.font.Font("./assets/fonts/Melon Honey.ttf", size)
    screen.blit(FONT.render(text, True, color), pos)
    del FONT

class Building:
    def __init__(self, name, size, pos, life):
        self.name = name
        self.img = None
        self.size = size
        self.pos = pos
        self.load()
        self.life = life

    def display(self, x, y):
        if x-2 <=self.pos[0] <= size_x/int(SIZE_CASE)+x and y-2 <=self.pos[1] <= size_y/int(SIZE_CASE)+y:
            screen.blit(self.img, ((self.pos[0]-x)*int(SIZE_CASE), (self.pos[1]-y)*int(SIZE_CASE)))

    def load(self):
        self.img = load_img(f"./assets/buildings/{self.name}.png", int(SIZE_CASE)*self.size[0] , int(SIZE_CASE)*self.size[1]) 



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

class Game:
    def __init__(self):
        self._map = Map()
        self._menu = Menu()
        self.ressources = {"bois" : (100, 75), "fer" : (200, 60), "eau" : (100, 60), "feu" : (60, 40), "acier" : (200, 30), "or" : (60, 12), "charbon" : (120, 79)}

    def display(self, screen):
        if self._menu.action in ("map", "edit"):
            self._map.display()
        self._menu.display(screen, self.ressources)
        pygame.display.update()

    def deplacement(self, x, y):
        self._map.pos[0] += x
        self._map.pos[1] += y
    
    def reload_images(self):
        self._map.reload_images()

game = Game()
continuer = True
DICT_BUILDINGS = {"Caserne" : Caserne, "Champs" : Champs, "Grenier" : Grenier}
while continuer:
    game.display(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            k = pygame.key.get_pressed()
            if k[pygame.K_F1]:
                game._menu.click("settings")
            if k[pygame.K_r]:
                game._menu.click("ressources")
            if k[pygame.K_e]:
                game._menu.click("edit")
            if game._menu.action in ("map", "edit"):
                if k[pygame.K_d]:
                    game._map.pos[0] += SENSIBILITY
                elif k[pygame.K_s]:
                    game._map.pos[1] += SENSIBILITY
                elif k[pygame.K_z]:
                    game._map.pos[1] -= SENSIBILITY
                elif k[pygame.K_q]:
                    game._map.pos[0] -= SENSIBILITY
        elif event.type == pygame.MOUSEWHEEL:
            event.y = -event.y
            if event.y < 0 and ZOOM >= 1.1 or event.y > 0 and ZOOM <= 1.9:
                old_zoom = ZOOM
                ZOOM = round(ZOOM + event.y/10, 1)
                SIZE_CASE = 1/ZOOM*SIZE_CASE/(1/old_zoom)
                game.reload_images()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.__dict__["button"] == 1:
            if game._menu.action == "edit":
                pos = list(pygame.mouse.get_pos())
                if MENU_EDIT_POS[0] < pos[0] and MENU_EDIT_POS[1] < pos[1]:
                    pos[0], pos[1] = pos[0] - MENU_EDIT_POS[0], pos[1] - MENU_EDIT_POS[1]
                    coord_case = (int(pos[0]/MENU_EDIT_POS[2]*3), 0)
                    index = 3*coord_case[1] + coord_case[0]
                    bat = LIST_BAT_MENU_EDIT[index]
                    game._menu.mem_tamp[0] = bat
        elif event.type == pygame.MOUSEBUTTONUP and event.__dict__["button"] == 1:
            pos = list(pygame.mouse.get_pos())
            if game._menu.action == "edit" and game._menu.mem_tamp is not None and game._menu.mem_tamp[0] is not None and (not MENU_EDIT_POS[0] < pos[0] or not MENU_EDIT_POS[1] < pos[1]):
                place_x = int((pos[0]+game._map.pos[0]*int(SIZE_CASE))//int(SIZE_CASE))
                place_y = int((pos[1]+game._map.pos[1]*int(SIZE_CASE))//int(SIZE_CASE))
                build = DICT_BUILDINGS[game._menu.mem_tamp[0]](place_x, place_y)
                if game._map.check_pos(build):
                    game._map.add_build(build)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                continuer = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            continuer = False