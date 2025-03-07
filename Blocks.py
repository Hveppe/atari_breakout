import pygame

pygame.init()

class blocks_class:
    width = 100
    height = 50

    def __init__(self, x, y, color, display):
        self.x = x
        self.y = y
        self.color = color
        self.display = display

    def draw(self):
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
