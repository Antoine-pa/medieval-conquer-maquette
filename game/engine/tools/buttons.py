import pygame
from . import cst, t

class Button:
    """
    class Button:
        classe gérant la conception de bouttons
    """
    def __init__(self, coords: tuple, text: str, thickness: int, background_color = cst("GREY_WHITE"), font_color = cst("BLACK")):
        self.coords = coords
        self.text = text
        self.thickness = thickness
        self.background_color = background_color
        self.font_color = font_color
    
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
        pygame.draw.rect(screen, self.background_color, (self.coords[0], self.coords[1], self.coords[2] - self.coords[0], self.coords[3] - self.coords[1]), 0)
        pygame.draw.rect(screen, self.font_color, (self.coords[0], self.coords[1], self.coords[2] - self.coords[0], self.coords[3] - self.coords[1]), self.thickness)
        t.text(screen, self.text, self.font_color, self.pos_text(), cst("SIZE_TEXT"))