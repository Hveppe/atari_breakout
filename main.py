import pygame
import math

from player_ball import ball_class, player_class

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

# Init af klasser
ball = ball_class(10, 10, display)
player = player_class(screenwith/2-50, screenheight-40, display)

# variabler
speed = 0

while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed += 1
            if event.key == pygame.K_LEFT:
                speed -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed -= 1
            if event.key == pygame.K_LEFT:
                speed += 1

    if collisionchecker_circle_square(ball, player):
        ball.velocity.x = -ball.velocity.x
        ball.velocity.y = -ball.velocity.y
            
    ball.update((screenwith, screenheight))
    player.update(speed, screenwith)
    player.draw()
    ball.draw()

    pygame.display.flip()