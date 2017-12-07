


import pygame
import numpy as np




# Turret Info
turret_margin = 10
turret_step_size = 0

turret_width = 15
turret_color = (255, 255, 0)

turret_border_width = 3
turret_border_color = (255, 110, 0)


# Bullet info
bullet_step_size = 5
bullet_color = (100, 100, 100)

bullet_width = 3
bullet_rate = 1000  # Milliseconds




#############################################################
# Main Turrets class object
#############################################################

class Turrets(object):

  # Initialize the object
  def __init__(self, screen):

    self.screen = screen

    # Matrix holding turret positions
    self.matrix = np.zeros((4,2)).astype(np.int)
    self.matrix[0,0] = 0
    self.matrix[0,1] = 0
    self.matrix[1,0] = self.screen.get_width()
    self.matrix[1,1] = 0
    self.matrix[2,0] = 0
    self.matrix[2,1] = self.screen.get_height()
    self.matrix[3,0] = self.screen.get_width()
    self.matrix[3,1] = self.screen.get_height()

    # Initialize empty list of bullets
    self.bullets = []


  # Advance the bullets
  def advance_bullets(self, qubert):
    # Aim new bullets at current location of qubert and fire off
    x = 5


  # Draw the turrets
  def draw(self):
    # Loop through all four turrets
    for i in range(self.matrix.shape[0]):
      # Draw turret i
      pygame.draw.circle(self.screen, turret_color, (self.matrix[i,0], self.matrix [i,1]), turret_width)
      pygame.draw.circle(self.screen, turret_border_color, (self.matrix[i,0], self.matrix[i,1]), turret_width, turret_border_width)


  def draw_bullets(self):

    for i in range(self.bullets.shape[0]):
      # Draw bullet i
      bt = pygame.Rect(bullet[i,0]-bullet_width, bullet[i,1]-bullet_width, 2*bullet_width, 2*bullet_width)
      self.screen.fill(bullet_color, rect=bt)



