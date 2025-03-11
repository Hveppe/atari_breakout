import pygame
import random
from Define import scale_faktor

pygame.init()
pygame.font.init()

class ball_class:
    speed = 10

    def __init__(self, x: float, y: float, display, color: tuple):
        self.x = x
        self.y = y
        self.radius = 10 * scale_faktor
        self.display = display
        self.color = color

        self.velocity = pygame.Vector2()
        self.velocity.xy = (2**(1/2))/2, (2**(1/2))/2

    def update(self, screen_size):
        self.x += self.velocity.x * self.speed
        self.y += self.velocity.y * self.speed

        screen_width, screen_height = screen_size

        # Checker kollision med kanterne af skærmen
        if self.x <= 0 or self.x >= screen_width:
            self.velocity.x = -self.velocity.x

            if self.x <= 0:
                self.x += self.radius
            elif self.x >= screen_width:
                self.x -= self.radius

        if self.y <= 0:
            self.velocity.y = -self.velocity.y

        if  self.y >= screen_height:
            return True
        return False
    
    def Ball_Blok_collision(self, blok):
        # Bestemmer den primærer kollisions retning (Det betyder hvilken side den rammer blokken)
        # Dette gøres ved at tjekke overlap i alle retninger

        overlap_venstre = self.x + self.radius - blok.x
        overlap_højre = blok.x + blok.width - (self.x - self.radius)
        overlap_top = self.y + self.radius - blok.y
        overlap_bund = blok.y + blok.height - (self.y - self.radius)

        # Finder det mindste overlap
        mindste_overlap = min(overlap_venstre, overlap_højre, overlap_top, overlap_bund)

        # Ændrer den pågældene vektor koordinat
        if mindste_overlap == overlap_højre or mindste_overlap == overlap_venstre:
            self.velocity.x = -self.velocity.x
        elif mindste_overlap == overlap_top or mindste_overlap == overlap_bund:
            self.velocity.y = -self.velocity.y

            
    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)


class player_class:
    width = 200 * scale_faktor
    height = 20 * scale_faktor
    radius = 30*scale_faktor
    speed = 10
    color = (255, 255, 255)
    Random = False
    
    def __init__(self, x: float, y: float, display, HP: int):
        self.x = x
        self.y = y
        self.display = display
        self.HP = HP

        self.velocity = pygame.Vector2()
        self.velocity.xy = 0, 0

        self.font = pygame.font.SysFont('Comic Sans MS', int(round(35*scale_faktor, 0)), bold=True, italic=False)
    
    def update(self, dir, screen_width):
        self.velocity.x = dir
        self.x += self.velocity.x * self.speed

        if self.x < 0:
            self.x = 0
        if self.x > screen_width-self.width:
            self.x = screen_width-self.width

        if self.Random is True:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.draw()
    
    def easter(self):
        self.width *= 2
        self.Random = True

    def draw(self):
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        pygame.draw.circle(self.display, (255, 255, 255), (self.radius+5*scale_faktor, self.radius+5*scale_faktor), self.radius)
        tekst = self.font.render(f"x{self.HP}", True, (0, 0, 0))
        self.display.blit(tekst, (self.radius-tekst.get_width()/2, self.radius-tekst.get_height()/2))
