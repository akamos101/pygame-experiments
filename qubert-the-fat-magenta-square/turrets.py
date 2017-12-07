


import pygame
import numpy as np
import math



# Turret Info
TURRET_MARGIN = 10

TURRET_WIDTH = 15
TURRET_COLOR = (255, 255, 0)

TURRET_BORDER_WIDTH = 3
TURRET_BORDER_COLOR = (255, 110, 0)


# Bullet info
BULLET_STEP_SIZE = 3
BULLET_COLOR = (100, 100, 100)

BULLET_WIDTH = 3
BULLET_RATE = 2000  # Milliseconds


#############################################################
# Main Turrets class object
#############################################################

class Turrets(object):

  # Initialize the object
  def __init__(self, screen):

    # Attach the screen object to the turret object for easy access
    self.screen = screen

    # Matrix holding turret positions
    self.matrix = np.zeros((4,2)).astype(np.int)
    self.matrix[0,0] = TURRET_MARGIN
    self.matrix[0,1] = TURRET_MARGIN
    self.matrix[1,0] = self.screen.get_width() - TURRET_MARGIN
    self.matrix[1,1] = TURRET_MARGIN
    self.matrix[2,0] = TURRET_MARGIN
    self.matrix[2,1] = self.screen.get_height() - TURRET_MARGIN
    self.matrix[3,0] = self.screen.get_width() - TURRET_MARGIN
    self.matrix[3,1] = self.screen.get_height() - TURRET_MARGIN

    # Initialize empty list of bullets
    self.bullets_last_time = pygame.time.get_ticks()
    self.bullets = np.asarray([])


  # Advance the bullets
  def advance_bullets(self, qubert):

    # Aim any new bullets at current location of qubert and fire off
    current_time = pygame.time.get_ticks()
    duration = current_time - self.bullets_last_time

    # Populate the bullet array if there aren't any already
    if np.array_equal(self.bullets, np.asarray([])):
        self.bullets = self.fire_bullets(qubert)
    else:
        # Advance the bullets that are there to their new positions
        self.bullets[:,0:2] = self.bullets[:,0:2] + self.bullets[:,2:4]

    # Check to see if Qubert has hit a bullet; if yes, set qubert.alive flag to 0
    for j in range(self.bullets.shape[0]):
      if np.linalg.norm(self.bullets[j,0:2] - [qubert.x, qubert.y]) <= (qubert.width + BULLET_WIDTH):
        print("Qubert got shot!")
        qubert.alive = False

    # If enough time has passed, create a new batch of bullets
    if duration > BULLET_RATE:
      self.bullets_last_time = current_time
      # Fire more bullets!
      self.bullets = np.vstack((self.bullets, self.fire_bullets(qubert)))

    return qubert



  # Draw the turrets
  def draw(self):
    # Loop through all four turrets
    for i in range(self.matrix.shape[0]):
      # Draw turret i
      pygame.draw.circle(self.screen, TURRET_COLOR, (self.matrix[i,0], self.matrix [i,1]), TURRET_WIDTH)
      pygame.draw.circle(self.screen, TURRET_BORDER_COLOR, (self.matrix[i,0], self.matrix[i,1]), TURRET_WIDTH, TURRET_BORDER_WIDTH)


  def draw_bullets(self):

    for i in range(self.bullets.shape[0]):
      # Draw bullet i
      bt = pygame.Rect(self.bullets[i,0]-BULLET_WIDTH, self.bullets[i,1]-BULLET_WIDTH, 2*BULLET_WIDTH, 2*BULLET_WIDTH)
      self.screen.fill(BULLET_COLOR, rect=bt)


  def fire_bullets(self, qubert):

    bullets = np.zeros((4,4))  # Four rows, one for each turret
                               # Four columns: x,y position
                               #               x,y direction vector to add
    bullets[0,0] = self.matrix[0,0] + TURRET_WIDTH
    bullets[0,1] = self.matrix[0,1] + TURRET_WIDTH
    bullets[1,0] = self.matrix[1,0] - TURRET_WIDTH
    bullets[1,1] = self.matrix[1,1] + TURRET_WIDTH
    bullets[2,0] = self.matrix[2,0] + TURRET_WIDTH
    bullets[2,1] = self.matrix[2,1] - TURRET_WIDTH
    bullets[3,0] = self.matrix[3,0] - TURRET_WIDTH
    bullets[3,1] = self.matrix[3,1] - TURRET_WIDTH

    bullets.astype(np.float)

    for i in range(4):
      # Get direction vector to qubert
      (vec_x, vec_y) = qubert.get_direction_vec(bullets[i,0], bullets[i,1])
      vec_length = np.linalg.norm([vec_x, vec_y])
      scale = float(BULLET_STEP_SIZE)/vec_length

      if vec_x >= 0.:
        bullets[i,2] = scale*vec_x
      else:
        bullets[i,2] = scale*vec_x
      if vec_y >= 0.:
        bullets[i,3] = scale*vec_y
      else:
        bullets[i,3] = scale*vec_y

    return bullets

