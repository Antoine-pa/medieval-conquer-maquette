import pygame
import time

BLACK = (0, 0, 0)
RED = (150, 0, 0)
WHITE = (255, 255, 255)
GREY_WHITE = (200, 200, 200)
GREY = (100, 100, 100)
SENSIBILITY = 0.4

pygame.init()
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w,screen_info.current_h))
size_x = screen_info.current_w
size_y = screen_info.current_h

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
        print(self.pos)
        screen.fill(WHITE)
        for x in range(0, size_x+50, 50):
            pygame.draw.line(screen, BLACK, (x-self.pos[0]%1*50, 0), (x-self.pos[0]%1*50, size_y))
            for y in range(0, size_y+50, 50):
                pygame.draw.line(screen, BLACK, (0, y-self.pos[1]%1*50), (size_x, y-self.pos[1]%1*50))
        for b in self.list_bat:
            b.display(*self.pos)
        pygame.display.update()

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
        self.img = load_img("Caserne1.png", 100, 100)

    def former(self):
        pass

    def display(self, x, y):
        print(x-2, self.pos[0], size_x/50+x)
        if x-2 <=self.pos[0] <= size_x/50+x and y-2 <=self.pos[1] <= size_y/50+y:
            screen.blit(self.img, ((self.pos[0]-x)*50, (self.pos[1]-y)*50))


class Game:
    def __init__(self):
        self._map = Map()
        self.ressources = {}

    def deplacement(self, x, y):
        self._map.pos[0] += x
        self._map.pos[1] += y

game = Game()
continuer = True
while continuer:
    game._map.display()
    for event in pygame.event.get():
        #Quitter
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                continuer = False
        if event.type == pygame.KEYDOWN:
            k = pygame.key.get_pressed()
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
        if event.type == pygame.QUIT:
            pygame.quit()
            continuer = False
