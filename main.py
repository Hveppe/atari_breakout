import pygame
import math

from player_blocks import ball_class

pygame.init()

screenwith, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwith, screenheight))
pygame.display.toggle_fullscreen()

def collisionchecker_circle_square(circle, square):
    # Finder afstanden mellem det tæteste punkt mellem square og circle
    closest_x = max(square.x, min(circle.x, square.x + square.width))
    closest_y = max(square.y, min(circle.y, square.y + square.height))

    distance = math.sqrt((circle.x - closest_x) ** 2 + (circle.y - closest_y) ** 2)

    # Checker om distancen er mindre eller det samme som radius
    if distance <= circle.radius:
        return True
    return False

ball = ball_class(10, 10, display)

while True:
    display.fill((0, 0, 0))
    
    ball.update((screenwith, screenheight))
    ball.draw()

    pygame.display.flip()