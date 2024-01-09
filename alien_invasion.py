import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gamestats import gamestats


class Alien_invasion():
    #  these class is used to overall the game assests and behaviour:
    def __init__(self):
    # initialize the game and create the game resources: 
        pygame.init()
        self.settings = Settings()
       
    # define the screen size , use set_mode method to display the screen.
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_Width = self.screen.get_rect().width
        self.settings.screen_Height = self.screen.get_rect().height
    # controlling the frame rate of game so we use the clock method in class
        self.clock = pygame.time.Clock()
    # use caption method for display the caption in pygame
        pygame.display.set_caption("ALIEN INVASION")
        # self.caption = pygame.display.get_caption()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = gamestats(self)
        self.create_fleet()
        collision = pygame.sprite.groupcollide(self.bullets , self.aliens , True , True)

    # set background color:
        self.bg_color = (255 ,255 , 255)
        
    def run_game(self ):
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullet()
            # self.bullets.update()
            self.update_aliens()
            # for bullet in self.bullets.copy():
            #       if bullet.rect.bottom <= 0:
            #             self.bullets.remove(bullet)
            # print(len(self.bullets))
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit() 
             elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RIGHT:
                      self.check_keydown_events(event)
             elif event.type == pygame.KEYUP:
                      self.check_keyup_events(event)
             elif event.type == pygame.K_UP:
                    self.check_K_UP(event)
             elif event.type == pygame.K_DOWN:
                    self.check_K_DOWN(event)


    def check_K_UP(self , event):
          if event.key == pygame.K_UP:
                    self.ship.moving_up = True
          elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
             
    def check_K_DOWN(self ,event):
          if event.key == pygame.K_UP:
                    self.ship.moving_up = False
          elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False        
    def check_keydown_events(self , event):
             
             
                if event.key == pygame.K_RIGHT:
                      self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                      sys.exit()
                elif event.key == pygame.K_SPACE:
                      self._fire_bullet()
                # redraw screen every timw with same exact time of loop run
    def check_keyup_events(self, event):
          if event.key == pygame.K_RIGHT:
                      self.ship.moving_right = False
          elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _fire_bullet(self):
          if len(self.bullets) < self.settings.bullet_allowed:
                
           new_bullet = Bullet(self)
           self.bullets.add(new_bullet)
    def update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
              bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    def update_bullet(self):
          self.bullets.update()
          for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)
          

    def bullet_alien_collision(self):
          collision = pygame.sprite.groupcollide(self.bullets , self.aliens , True , True)
      #     check if aliens group is empty than empty the bullet and create new fleet
          if not self.aliens:
                self.bullets.empty()
                self.create_fleet()
                

    def create_fleet(self):
          alien = Alien(self)
          alien_width , alien_height = alien.rect.size
          current_x  , current_y = alien_width   , alien_height
          while current_y < (self.settings.screen_Height - 3 * alien_height):
            while current_x < (self.settings.screen_Width - 2 * alien_width):
                self.create_alien(current_x , current_y)
                current_x += 2* alien_width

            current_x = alien_width
            current_y += 2 * alien_height
    def create_alien(self , current_x , current_y):
                new_Alien = Alien(self)
                new_Alien.x  = current_x 
                new_Alien.rect.x  = current_x
                new_Alien.rect.y = current_y
                self.aliens.add(new_Alien)
                # current_x += 2* alien_width
    def check_fleet_edges(self):
          for alien in self.aliens.sprites():
                if alien.check_edge():
                      self.change_fleet_direction()
                      break
                
    def change_fleet_direction(self):
          for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed
          self.settings.fleet_direction *= -1

        # this function is increment the alien on y axis wiht drop speed
        # 10 and fleet direction is multiply by  minus one

    def update_aliens(self):
          self.check_fleet_edges()
          self.aliens.update()
          if pygame.sprite.spritecollideany(self.ship,self.aliens):
           self.ship_hit()
          
    def ship_hit(self):
      #     respond the ship if it is hit by alien. decerment to 1 ship_limit
          self.stats.ship_left   =-1      

      # rid of any remaning bullets and aliens
          self.bullets.empty()
          self.aliens.empty()

      # creare a new fleet and center the ship position:
          self.create_fleet()
          self.ship.center_ship()
      # pause the game:
          sleep(0.5)

    def aliens_hit_bottom(self):
      
      
      for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_Height:
                  self.ship_hit()
                  break

if __name__ == "__main__":
  ai = Alien_invasion()
  ai.run_game()

