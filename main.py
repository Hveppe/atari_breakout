import pygame
import math

from player_ball import ball_class, player_class
from Blocks import blocks_class

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
balls = [ball_class(screenwith/2-10, screenheight-80, display)]
player = player_class(screenwith/2-50, screenheight-70, display)

# Laver blokene (Den er dårlig ikke mob)
y = 40
colors = [(255, 51, 51), (255, 153, 102), (255, 255, 51), (153, 255, 51), (51, 51, 204)]
blocks = []
for i in range(10):
    x = screenwith/2 - 850

    for _ in range(16):
        blocks.append(blocks_class(x, y, colors[i % len(colors)], display))
        x += 110

    y += 55

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

    
    for ball in balls:
        # Kode som der håndterer kollision mellem balls og player 
        if collisionchecker_circle_square(ball, player):
            ball.velocity.y = -ball.velocity.y
            
        if ball.update((screenwith, screenheight)):
            balls.remove(ball)
        
        
        ball.draw()

    for blok in blocks:
        
        blok.draw()

        for ball in balls:
            if collisionchecker_circle_square(ball, blok):
                ball.velocity.y = -ball.velocity.y
                #ball.velocity.x = -ball.velocity.x
                blocks.remove(blok)
    
    player.update(speed, screenwith)
    player.draw()

    if len(balls) == 0:
        exit()

    pygame.display.flip()