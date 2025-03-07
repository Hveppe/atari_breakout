import pygame

pygame.init()

class ball_class:
    color = (255, 255, 255)
    speed = 10

    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.radius = 10
        self.display = display

        self.velocity = pygame.Vector2()
        self.velocity.xy = (2**(1/2))/2, (2**(1/2))/2

    def update(self, screen_size):
        self.x += self.velocity.x * self.speed
        self.y += self.velocity.y * self.speed

        screen_width, screen_height = screen_size

        if self.x <= 0 or self.x >= screen_width:
            self.velocity.x = -self.velocity.x
        
        if self.y <= 0:
            self.velocity.y = -self.velocity.y

        if  self.y >= screen_height:
            return True
        return False
            
    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)


class player_class:
    width = 100
    height = 20
    speed = 10
    color = (255, 255, 255)
    
    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.display = display

        self.velocity = pygame.Vector2()
        self.velocity.xy = 0, 0
    
    def update(self, dir, screen_width):
        self.velocity.x = dir
        self.x += self.velocity.x * self.speed

        if self.x < 0:
            self.x = 0
        if self.x > screen_width-self.width:
            self.x = screen_width-self.width



    def draw(self):
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
