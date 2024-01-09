import sys
import pygame

class Settings:


    def __init__(self):
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.screen_Width = 800
        self.screen_Height = 1200
        self.bg_color = (255 ,255 ,255)
        # bullet settings:
        self.bullet_speed = 2.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color  = (60, 60, 60)
        self.bullet_allowed = 3
        # self.clock = pygame.time.Clock()        
        # alien settings:
        self.alien_speed = 1.0
        # settings for fleet meaning of fleet is  alien means when bullet
        # touch the alien then alien will be disappear.
        # direction is on down point alien is move to the direction
        # of x means into the spacehip. in thus define the settings of
        # fleet speed:
        self.fleet_drop_speed = 10
        # fleet direction one represents the right and -1 represents the left

        self.fleet_direction = 1