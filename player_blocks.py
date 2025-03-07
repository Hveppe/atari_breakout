import pygame

pygame.init()

class ball_class:
    color = (255, 255, 255)

    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.radius = 10
        self.display = display

        self.velocity = pygame.Vector2()
        self.velocity.xy = 0.5, 0.5

    def update(self, screen_size):
        self.x += self.velocity.x
        self.y += self.velocity.y

        screen_width, screen_height = screen_size

        if self.x <= 0 or self.x >= screen_width:
            self.velocity.x = -self.velocity.x
        
        if self.y <= 0 or self.y >= screen_height:
            self.velocity.y = -self.velocity.y
            
    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)


class player_class:
    width = 100
    height = 100
    color = (255, 255, 255)
    
    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.display = display

        self.velocity = pygame.Vector2()
        self.velocity.xy = 0, 0
    
    def update(self, speed):
        self.velocity.x = speed

    def draw(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y), (self.width, self.height))
