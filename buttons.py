import pygame
from tools import *

class Button:
    """
    class Button:
        classe gérant la conception de bouttons
    """
    def __init__(self, coords: tuple, text: str, thickness: int):
        self.coords = coords
        self.text = text
        self.thickness = thickness
    
    def __repr__(self):
        return f"coords : {self.coords}, text : {self.text}, thickness : {self.thickness}"

    def collidepoint(self, pos) -> bool:
        """
        check si le click est sur le boutton
        """
        return self.coords[0] <= pos[0] <= self.coords[2] and self.coords[1] <= pos[1] <= self.coords[3]

    def pos_text(self) -> tuple: #à modifier, marche pas vraiment
        """
        retourne la position du texte à afficher
        """
        return (self.coords[0]+self.thickness+3, self.coords[3]-self.thickness-1.25*cst("SIZE_TEXT"))
    
    def display(self, screen):
        """
        affiche le boutton
        """
        pygame.draw.rect(screen, cst("BLACK"), (self.coords[0], self.coords[1], self.coords[2] - self.coords[0], self.coords[3] - self.coords[1]), self.thickness)
        t.text(screen, self.text, cst("BLACK"), self.pos_text(), cst("SIZE_TEXT"))