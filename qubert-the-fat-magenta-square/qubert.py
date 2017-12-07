


import pygame





#############################################################
# CONSTANTS
#############################################################
STEP_SIZE = 2 # Step size to control "speed" of qbert
SQUARE_WIDTH = 10
SQUARE_COLOR = (255, 0, 255)

BORDER_WIDTH = 3
BORDER_COLOR = (150, 0, 150)




#############################################################
# Main Qubert class object
#############################################################
class Qubert(object):

  # Initialize the object
  def __init__(self, screen):
    self.screen = screen                # Screen that Qubert is drawn on
    self.x = self.screen.get_width() / 2  # Initial x-coordinate
    self.y = self.screen.get_height() / 2 # Initial y-coordinate
    self.step_size = STEP_SIZE          # Step size to control "speed" of qbert
    self.width = SQUARE_WIDTH
    self.alive = True

    # Initial direction Qubert is moving: up
    self.direction_x = 0
    self.direction_y = -1*self.step_size


  # Advance the position of Qubert
  def advance_position(self):
    # Move Qbert to the new location
    self.x += self.direction_x
    self.y += self.direction_y

  # Draw the object on the screen
  def draw(self):

    # Draw Qubert the fat magenta square
    qb = pygame.Rect(self.x - SQUARE_WIDTH, self.y - SQUARE_WIDTH, 2*SQUARE_WIDTH, 2*SQUARE_WIDTH)
    qb_border = pygame.Rect(
      self.x - SQUARE_WIDTH - BORDER_WIDTH, 
      self.y - SQUARE_WIDTH - BORDER_WIDTH, 
      2*(SQUARE_WIDTH + BORDER_WIDTH), 
      2*(SQUARE_WIDTH + BORDER_WIDTH))

    self.screen.fill(BORDER_COLOR, rect=qb_border)
    self.screen.fill(SQUARE_COLOR, rect=qb)

  # Get the vector from a point to Qubert's current location
  def get_direction_vec(self, x, y):
    vec_x = float(self.x) - float(x)
    vec_y = float(self.y) - float(y)
    return (vec_x, vec_y)


