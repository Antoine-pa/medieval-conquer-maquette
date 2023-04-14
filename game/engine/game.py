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
        self._menu.update_buttons(self._map)
        self.reload_images()

    def __repr__(self):
        return f"Game :\n - {self._map}\n\n - {self._menu}"

    def deplacement(self, x: int, y: int) -> None:
        """
        gère les déplacement dans la map
        """
        self._map.pos[0] += x
        self._map.pos[1] += y

    def display(self, screen: pygame.surface.Surface) -> None:
        """
        gère l'affichage du jeu
        """
        if self._menu.action.startswith("map") or self._menu.action.startswith("edit"):
            self._map.display(screen)
        self._menu.display(screen, self._map)
        pygame.display.update()
    
    def reload_images(self) -> None:
        """
        lance le rechargement des images
        """
        self._map.reload_images()
        if self._menu.mem_tamp is not None:
            for c in self._menu.mem_tamp["list_build"].items():
                builds = []
                for b in c[1]["add"].values():
                    if b not in builds:
                        b.load()
                        builds.append(b)
                        
    def update_production(self) -> None:
        for c in self._map.dict_kind_build.items():
            for build in c[1].get("production", []):
                build.update()
    
