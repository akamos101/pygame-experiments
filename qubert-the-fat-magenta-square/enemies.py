


import pygame
import random
import numpy as np
import math


# Enemy info.
enemy_margin = 5    # Margin for enemy box
enemy_step_size = 1 # Step size to control "speed" of enemys

enemy_width = 15
enemy_color = (0, 0, 255)

enemy_border_width = 3
enemy_border_color = (0, 0, 150)




#############################################################
# Main Enemies class object
#############################################################

class Enemies(object):

  # Initialize the object
  def __init__(self, screen, num_enemies):

    self.screen = screen

    # Matrix holding enemy positions and whether or not enemy is dead
    self.matrix = np.zeros((num_enemies, 3)).astype(np.int)
    for i in range(num_enemies):
      # Choose random numbers in {0,1} to determine top/bottom/left/right
      # side of a rectangle centered about the initial position of Qbert
      type_1 = round(random.random())
      type_2 = round(random.random())
      # Depending on which side chosen, choose a random point on that side
      if type_1:
        if type_2:
          self.matrix[i,0] = random.randint(enemy_margin, screen.get_width() - enemy_margin)
          self.matrix[i,1] = enemy_margin
        else:
          self.matrix[i,0] = random.randint(enemy_margin, screen.get_width() - enemy_margin)
          self.matrix[i,1] = screen.get_height() - enemy_margin
      else:
        if type_2:
          self.matrix[i,0] = enemy_margin
          self.matrix[i,1] = random.randint(enemy_margin, screen.get_height() - enemy_margin)
        else:
          self.matrix[i,0] = screen.get_width() - enemy_margin
          self.matrix[i,1] = random.randint(enemy_margin, screen.get_height() - enemy_margin)


  # Advance the enemy positions
  def advance_positions(self, qubert, turrets):

    # Loop through all of the enemies
    for i in range(self.matrix.shape[0]):

      # Set new enemy position:
      # Go an enemy_step_size pixel length in a straight line toward Qbert

      # Get vector from Enemy to Qbert
      (vec_x, vec_y) = qubert.get_direction_vec(self.matrix[i,0], self.matrix[i,1])

      # Compute the length of the vector
      vec_length = np.linalg.norm([vec_x, vec_y])

      # Check to see if Qbert has hit an enemy; if yes, terminate game
      if vec_length < qubert.width+enemy_width:
        print("You've been hit by enemy #%d!" % (i+1))
        qubert.alive = False

      # Check to see if enemy has hit a bullet; if yes, set enemy died flag to 1
      for j in range(turrets.bullets.shape[0]):
        if np.linalg.norm(turrets.bullets[j,0:2] - self.matrix[i,0:2]) <= (enemy_width + 2):
          self.matrix[i,2]=1

      # Scale the vector to the length enemy_step_size
      # Remember to convert step size to float to do decimal division
      scale = float(enemy_step_size)/vec_length

      # Remember to convert back to integers to set position
      # Round up if positive direction, round down if negative direction
      if vec_x >= 0.:
        self.matrix[i,0] += int(math.ceil(scale*vec_x))
      else:
        self.matrix[i,0] += int(math.floor(scale*vec_x))
      if vec_y >= 0.:
        self.matrix[i,1] += int(math.ceil(scale*vec_y))
      else:
        self.matrix[i,1] += int(math.floor(scale*vec_y))

    # Only keep the enemies that are still alive
    self.matrix = self.matrix[(self.matrix[:,2]==0),:]

    return qubert



  # Draw the enemies
  def draw(self):

    for i in range(self.matrix.shape[0]):
      # Draw enemy i
      pygame.draw.circle(self.screen, enemy_color, (self.matrix[i,0], self.matrix[i,1]), enemy_width)
      pygame.draw.circle(self.screen, enemy_border_color, (self.matrix[i,0], self.matrix[i,1]), enemy_width, enemy_border_width)



