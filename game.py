from map import Map
from menu import Menu
from tools import *
import pygame

class Game:
    """
    class Game:
        class gérant la map et les menu
    """
    def __init__(self):
        self._map = Map()
        self._menu = Menu()
        self.ressources = {"bois" : (100, 56), "fer" : (200, 60), "eau" : (100, 60), "feu" : (60, 40), "acier" : (200, 30), "or" : (60, 12), "charbon" : (120, 79)}

    def __repr__(self):
        return f"Game :\n - {self._map}\n\n - {self._menu}\n\n - ressources : {self.ressources}"

    def display(self, screen):
        """
        gère l'affichage du jeu
        """
        if self._menu.action == "map" or self._menu.action.startswith("edit"):
            self._map.display(screen)
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
    
