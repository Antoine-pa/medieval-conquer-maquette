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
LIST_BAT_MENU_EDIT = ["Caserne1", "Caserne1", "Caserne1"]
ZOOM = 1


def load_img(name, x, y):
    img = pygame.image.load(name)
    img = pygame.transform.scale(img,(x, y))
    return img


class Map:
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.pos = [self.x/2, self.y/2]
        self.list_bat = [Caserne(503, 506)]

    def display(self):
        screen.fill(WHITE)
        for x in range(0, size_x+50, 50):
            pygame.draw.line(screen, BLACK, (x-self.pos[0]%1*50, 0), (x-self.pos[0]%1*50, size_y))
            for y in range(0, size_y+50, 50):
                pygame.draw.line(screen, BLACK, (0, y-self.pos[1]%1*50), (size_x, y-self.pos[1]%1*50))
        for b in self.list_bat:
            b.display(*self.pos)

class Menu:
    def __init__(self):
        self.action = "map"
        self.mem_tamp = None

    def click(self, act):
        if self.action != act:
            if act == "edit":
                self.mem_tamp = [None, None]
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
            Text(str(res[1][0])+"/"+str(res[1][1])+" ("+str(round(ratio*100, 2))+"%)", BLACK, (size_x/2+size_x/8, size_y/4+size_y/(6*len(ressources))+i*size_y/(2*len(ressources))), int(size_y/(6*len(ressources))))

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


class UsineCanon:
    def __init__(self):
        self.list_bat = []
        self.max = 2
        self.file = ""

    def construire(self):
        pass

class Canon:
    def __init__(self):
        self.type = ""
        self.deg = 0


class Caserne:
    def __init__(self, x, y):
        self.list_unit = []
        self.max = 5
        self.pos = [x, y]
        self.img = load_img("./assets/buildings/Caserne1.png", 100, 100)

    def former(self):
        pass

    def display(self, x, y):
        if x-2 <=self.pos[0] <= size_x/50+x and y-2 <=self.pos[1] <= size_y/50+y:
            screen.blit(self.img, ((self.pos[0]-x)*50, (self.pos[1]-y)*50))


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


game = Game()
continuer = True
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
                """
                if k[pygame.K_z] and k[pygame.K_d]:
                    coord_sous_fenetre[0] -= int((2**0.5*SENSIBILITY)/2)
                    coord_sous_fenetre[1] += int((2**0.5*SENSIBILITY)/2)
                elif k[pygame.K_z] and k[pygame.K_q]:
                    coord_sous_fenetre[0] -= int((2**0.5*SENSIBILITY)/2)
                    coord_sous_fenetre[1] -= int((2**0.5*SENSIBILITY)/2)
                elif k[pygame.K_q] and k[pygame.K_s]:
                    coord_sous_fenetre[0] += int((2**0.5*SENSIBILITY)/2)
                    coord_sous_fenetre[1] -= int((2**0.5*SENSIBILITY)/2)
                elif k[pygame.K_s] and k[pygame.K_d]:
                    coord_sous_fenetre[0] += int((2**0.5*SENSIBILITY)/2)
                    coord_sous_fenetre[1] += int((2**0.5*SENSIBILITY)/2)
                """
                if k[pygame.K_d]:
                    game._map.pos[0] += SENSIBILITY
                elif k[pygame.K_s]:
                    game._map.pos[1] += SENSIBILITY
                elif k[pygame.K_z]:
                    game._map.pos[1] -= SENSIBILITY
                elif k[pygame.K_q]:
                    game._map.pos[0] -= SENSIBILITY
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game._menu.action == "edit":
                pos = list(pygame.mouse.get_pos())
                if MENU_EDIT_POS[0] < pos[0] and MENU_EDIT_POS[1] < pos[1]:
                    pos[0], pos[1] = pos[0] - MENU_EDIT_POS[0], pos[1] - MENU_EDIT_POS[1]
                    coord_case = (int(pos[0]/MENU_EDIT_POS[2]*3), 0)
                    index = 3*coord_case[1] + coord_case[0]
                    bat = LIST_BAT_MENU_EDIT[index]
                    print(bat, index)




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                continuer = False
        if event.type == pygame.QUIT:
            pygame.quit()
            continuer = False
