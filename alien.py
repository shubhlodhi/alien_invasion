import pygame
from pygame.sprite import  Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings  = ai_game.settings

        self.image = pygame.image.load("images/alien.png")
        desired_width = 80
        desired_height = 60
        
        # Resize the image to fit the desired dimensions
        self.image = pygame.transform.scale(self.image, (desired_width, desired_height))
        self.rect = self.image.get_rect()
# start new alien near the top left of screen
        self.rect.x  = self.rect.width
        self.rect.y  = self.rect.height
#  store the alien exact position
        self.x  = float(self.rect.x)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
    

# now add the update function in a class to update the position of alien:
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
