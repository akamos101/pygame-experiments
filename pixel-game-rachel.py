#! /usr/bin/env python

# Move a single pixel around the screen without crashing against the borders.

import pygame
import random
import numpy as np
import math

# Window dimensions.
width = 640
height = 400

# Qbert info
qb_x = width / 2    # Initial x-coordinate
qb_y = height / 2   # Initial y-coordinate

qbert_step_size = 2 # Step size to control "speed" of qbert

qb_width = 10
qb_color = (255, 0, 255)

qb_border_width = 3
qb_border_color = (150, 0, 150)

# Enemy info.
enemy_margin = 5    # Margin for enemy box
enemy_step_size = 1 # Step size to control "speed" of enemys

enemy_width = 15
enemy_color = (0, 0, 255)

enemy_border_width = 3
enemy_border_color = (0, 0, 150)

num_enemies = 20     # Number of enemies to spawn


# Turret Info
turret_margin = 10
turret_step_size = 0

turret_width = 15
turret_color = (255, 255, 0)

turret_border_width = 3
turret_border_color = (255, 110, 0)




# Initialize enemy positions
enemy = np.zeros((num_enemies, 2)).astype(np.int)
for i in range(num_enemies):
  # Choose random numbers in {0,1} to determine top/bottom/left/right
  # side of a rectangle centered about the initial position of Qbert
  type_1 = round(random.random())
  type_2 = round(random.random())
  # Depending on which side chosen, choose a random point on that side
  if type_1:
    if type_2:
      enemy[i,0] = random.randint(enemy_margin, width - enemy_margin)
      enemy[i,1] = enemy_margin
    else:
      enemy[i,0] = random.randint(enemy_margin, width - enemy_margin)
      enemy[i,1] = height - enemy_margin
  else:
    if type_2:
      enemy[i,0] = enemy_margin
      enemy[i,1] = random.randint(enemy_margin, height - enemy_margin)
    else:
      enemy[i,0] = width - enemy_margin
      enemy[i,1] = random.randint(enemy_margin, height - enemy_margin)



# Background info:
bg_color = (100, 255, 100)



def draw_qbert():

  # Create qbert
  qb = pygame.Rect(qb_x - qb_width, qb_y - qb_width, 2*qb_width, 2*qb_width)
  qb_border = pygame.Rect(
    qb_x - qb_width - qb_border_width, 
    qb_y - qb_width - qb_border_width, 
    2*(qb_width + qb_border_width), 
    2*(qb_width + qb_border_width))

  screen.fill(qb_border_color, rect=qb_border)
  screen.fill(qb_color, rect=qb)



def draw_enemy(i):

  # Draw the enemy
  pygame.draw.circle(screen, enemy_color, (enemy[i,0], enemy[i,1]), enemy_width)
  pygame.draw.circle(screen, enemy_border_color, (enemy[i,0], enemy[i,1]), enemy_width, enemy_border_width)



# Direction of the pixel.
dir_x = 0
dir_y = -1*qbert_step_size

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:

  # Move Qbert to the new location
  qb_x += dir_x
  qb_y += dir_y

  # Check to see if Qbert has hit an edge; if yes, terminate game
  if qb_x <= 0 or qb_x >= width or qb_y <= 0 or qb_y >= height:
      print("Crash!")
      running = False

  # Re-paint the background color to wipe out old graphics
  screen.fill(bg_color)
  # Draw Qbert
  draw_qbert()

  # Loop through all of the enemies
  for i in range(num_enemies):

    # Set new enemy position:
    # Go an enemy_step_size pixel length in a straight line toward Qbert

    # Get vector from Enemy to Qbert
    # Use floats for higher precision later
    vec_x = float(qb_x - enemy[i,0])
    vec_y = float(qb_y - enemy[i,1])

    # Compute the length of the vector
    vec_length = np.linalg.norm([vec_x, vec_y])

    # Check to see if Qbert has hit an enemy; if yes, terminate game
    if vec_length < qb_width+enemy_width:
      print("You've been hit by enemy #%d!" % (i+1))
      running = False

    # Scale the vector to the length enemy_step_size
    # Remember to convert step size to float to do decimal division
    scale = float(enemy_step_size)/vec_length

    # Remember to convert back to integers to set position
    # Round up if positive direction, round down if negative direction
    if vec_x >= 0.:
      enemy[i,0] += int(math.ceil(scale*vec_x))
    else:
      enemy[i,0] += int(math.floor(scale*vec_x))
    if vec_y >= 0.:
      enemy[i,1] += int(math.ceil(scale*vec_y))
    else:
      enemy[i,1] += int(math.floor(scale*vec_y))

    # Draw the enemy
    draw_enemy(i)

  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
              dir_x = 0
              dir_y = -1*qbert_step_size
          elif event.key == pygame.K_DOWN:
              dir_x = 0
              dir_y = 1*qbert_step_size
          elif event.key == pygame.K_LEFT:
              dir_x = -1*qbert_step_size
              dir_y = 0
          elif event.key == pygame.K_RIGHT:
              dir_x = 1*qbert_step_size
              dir_y = 0

  pygame.display.flip()
  clock.tick(50)





