import pygame
from engine import Game, t, cst, DICT_BUILDINGS


class App:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((screen_info.current_w-100,screen_info.current_h-100))
        size_x = screen_info.current_w-100
        size_y = screen_info.current_h-100
        t.set_all_const(size_x, size_y)
        self.process = True
        self.game = Game()
        t.load_map(self.game._map, DICT_BUILDINGS)

    def main(self):
        while self.process:
            self.game.display(self.screen)
            self.game.update_production()
            for event in pygame.event.get():
                try:
                    pos = list(pygame.mouse.get_pos())
                except:
                    pass
                if event.type == pygame.KEYDOWN: #à l'appui d'une touche
                    k = pygame.key.get_pressed()
                    if self.game._menu.action == "map" or self.game._menu.action.startswith("edit"):
                        # déplacement sur la map
                        if k[pygame.K_d]:
                            self.game._map.pos[0] += cst("SENSIBILITY")
                        elif k[pygame.K_s]:
                            self.game._map.pos[1] += cst("SENSIBILITY")
                        elif k[pygame.K_z]:
                            self.game._map.pos[1] -= cst("SENSIBILITY")
                        elif k[pygame.K_q]:
                            self.game._map.pos[0] -= cst("SENSIBILITY")
                elif event.type == pygame.MOUSEWHEEL:
                    #scroll pour le zoom
                    zoom = self.game._map.zoom(-event.y)
                    if zoom:
                        self.game.reload_images()
                elif event.type == pygame.MOUSEBUTTONUP and event.__dict__["button"] == 1: #lors d'un clic gauche
                    self.game._menu.click(pos, self.game._map)
                elif event.type == pygame.KEYUP: #lors de l'appui d'une touche
                    if k[pygame.K_F1]:
                        self.game._menu.set_action("settings", self.game._map)
                    if k[pygame.K_r]:
                        self.game._menu.set_action("ressources", self.game._map)
                    if k[pygame.K_e]:
                        self.game._menu.set_action("edit", self.game._map)
                    if self.game._menu.mem_tamp is not None and self.game._menu.mem_tamp["bat"] is not None:
                        if k[pygame.K_UP]:
                            self.game._menu.mem_tamp["bat"]["angle"] = 90
                        if k[pygame.K_RIGHT]:
                            self.game._menu.mem_tamp["bat"]["angle"] = 0
                        if k[pygame.K_DOWN]:
                            self.game._menu.mem_tamp["bat"]["angle"] = 270
                        if k[pygame.K_LEFT]:
                            self.game._menu.mem_tamp["bat"]["angle"] = 180
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        self.process = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    self.process = False

App().main()