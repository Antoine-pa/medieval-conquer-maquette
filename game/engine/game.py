from . import Menu, Map
import pygame

class Game:
    """
    class Game:
        class gérant la map et les menu
    """
    def __init__(self):
        self._map = Map()
        self._menu = Menu()

    def __repr__(self):
        return f"Game :\n - {self._map}\n\n - {self._menu}"

    def display(self, screen):
        """
        gère l'affichage du jeu
        """
        if self._menu.action == "map" or self._menu.action.startswith("edit"):
            self._map.display(screen)
        self._menu.display(screen, self._map.pos)
        pygame.display.update()
    
    def update_production(self):
        for build in self._map.list_build:
            if build.kind == "production":
                build.update()

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
