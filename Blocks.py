import pygame
from Define import scale_faktor

pygame.init()

class blocks_class:
    width = 100*scale_faktor
    height = 50*scale_faktor
    
    def __init__(self, x: float, y: float, color: tuple, display):
        self.x = x
        self.y = y
        self.color = color
        self.display = display

    def draw(self):
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
