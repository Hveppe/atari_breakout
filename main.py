"""
##########################################
#                                        #
#             Atari Breakout             #
#            Skrevet i Python            #
#                                        #
#              Python koden              #
#            skrevet af Hveppe           #
#                                        #
#   Orginale spil skrevet af Atari inc.  #
#                                        #
##########################################
"""


import pygame
import math
import random


from player_ball import ball_class, player_class
from Blocks import blocks_class
from Define import scale_faktor

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

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

# Skaber player og den første ball
balls = [ball_class(screenwith/2-10, screenheight-(90*scale_faktor), display, (255, 255, 255))]
balls[0].velocity.xy = 0, 0

player = player_class(screenwith/2-50, screenheight-70, display, 3)

# Laver blokene
colors = [(255, 51, 51), (255, 153, 102), (255, 255, 51), (153, 255, 51), (51, 51, 204)]
blocks = []

def more_bloks():
    y = 55 * scale_faktor
    for i in range(8): # Laver blokke hen af y-aksen
        x = screenwith/2 - (875*scale_faktor)

        for _ in range(16): # Laver blokke hen af x-aksen
            blocks.append(blocks_class(x, y, colors[i % len(colors)], display))
            x += 110 * scale_faktor

        y += 55 * scale_faktor

Font = pygame.font.SysFont('Comic Sans MS', int(round(40*scale_faktor, 0)), bold=True, italic=False)
speed = score = 0
right = left = False
bloks_to_remove = []
fired = False

while True:
    clock.tick(60) # Låser framerate til 60 fps
    display.fill((0, 0, 0))

    # Controls
    # TODO: Lav noget bedre
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and speed != 1:
                right = True
                speed += 1
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and speed != -1:
                left = True
                speed -= 1
            if fired is False and (event.key == pygame.K_UP or event.key == pygame.K_w):
                fired = True

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and right:
                right = False
                speed -= 1
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and left:
                left = False
                speed += 1
    
    for ball in balls:
        # Kode som der håndterer kollision mellem balls og player 
        if collisionchecker_circle_square(ball, player):
            
            # Bevægelse bestemmes ud fra hvor den rammer player 
            ball.velocity.x = (ball.x-(player.x+(player.width/2)))/(player.width/2)

            try:
                ball.velocity.y = -math.sqrt(1-(ball.velocity.x**2))
            except ValueError:
                ball.velocity.x = 0.99
                ball.velocity.y = -math.sqrt(1-(ball.velocity.x**2))

        if ball.update((screenwith, screenheight)):
            balls.remove(ball)
        
        ball.draw()

    # Her håndterer programmet blokkene og deres interaktioner med balls
    bloks_to_remove.clear()
    for blok in blocks:

        for ball in balls:
            blok.draw()
            
            if collisionchecker_circle_square(ball, blok):
                
                # basret på hvor bolden rammer blokken afgår ændring af vektoren
                if blok.y < ball.y < blok.y + blok.height:
                    ball.velocity.x = -ball.velocity.x
                else:
                    ball.velocity.y = -ball.velocity.y

                # Power up
                try:
                    if random.randint(1, 20) == 1:
                        balls.append(ball_class(blok.x+(blok.width/2), blok.y+(blok.height/2), display, blok.color))
                    bloks_to_remove.append(blok)

                    score += 4
                        
                except ValueError:
                    pass

    for blok in bloks_to_remove:
        try:
            blocks.remove(blok)
        except ValueError:
            pass
    
    # Handlinger som påvirker player
    player.update(speed, screenwith)

    if fired is False:
        balls[0].x, balls[0].y = player.x + player.width/2, player.y

    # Diverse event check
    if len(balls) == 0:
        if player.HP > 0:
            player.HP -= 1
            fired = False
            balls.append(ball_class(player.x + player.width/2, player.y, display, (255, 255, 255)))
        else:
            exit()

    if len(blocks) == 0:
        more_bloks()

    if score >= 1976 and player.Random is False:
       player.easter()

    # Display af score
    tekst = Font.render(f'{score}'.zfill(4), True, (255, 255, 255))
    display.blit(tekst, (screenwith/2 - tekst.get_width()/2, 0))

    pygame.display.flip()