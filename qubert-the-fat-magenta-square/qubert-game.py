#! /usr/bin/env python

#############################################################
# Qubert the Fat Magenta Square
#
# Copyright (C) 2017 Spencer Cobain and Rachel Levanger
# Authors: 
#           Spencer Cobain <akamosmuffin@gmail.com>
#           Rachel Levanger <rachel.levanger@gmail.com>
#############################################################


# Import packages needed by the game play
import pygame
import numpy as np

# Package needed for parsing arguments
from optparse import OptionParser

# Import the helper python files for all of the agent objects
import enemies as qb_enemies
import screen as qb_screen
import qubert as qb_qubert
import turrets as qb_turrets



#############################################################
# Parse the options supplied by the user
#############################################################

parser = OptionParser('usage: -e num_enemies')

# Define the options
parser.add_option("-e", dest="num_enemies",
                  help="Number of enemies to spawn")

# Parse the options
(options, args) = parser.parse_args()

# Populate variables corresponding to user-supplied options
num_enemies = int(options.num_enemies)  # Number of enemies to spawn




#############################################################
# Initialize Objects
#############################################################

# Game container & objects
screen = qb_screen.initialize()
clock = pygame.time.Clock()

# Active agents in game
qubert = qb_qubert.Qubert(screen)
enemies = qb_enemies.Enemies(screen, num_enemies)
turrets = qb_turrets.Turrets(screen)


#############################################################
# Set initial game-play state variables
#############################################################

running = True
paused = False



#############################################################
# Game play
#############################################################

while running:

  if not paused:

    # Move Qbert to the new location
    qubert.advance_position()

    # Check to see if Qbert is on the screen; if not, terminate the game
    if not qb_screen.onscreen(screen, qubert.x, qubert.y):
        print("Crash!")
        running = False

    # Advance the bullet positions and add fire additional bullets
    turrets.advance_bullets(qubert)

    # Advance the enemy positions
    # Kill them off it they hit bullets
    # Also kill off Qubert if he hits an enemy
    qubert = enemies.advance_positions(qubert)
    if not qubert.alive:
      running = False

    # Repaint the background color to wipe out old graphics
    qb_screen.paint_background(screen)

    # Draw all of the agents
    turrets.draw()
    enemies.draw()
    qubert.draw()

  # Check for keypress events in the game
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      elif event.type == pygame.KEYDOWN:
          paused = False
          if event.key == pygame.K_UP:
              qubert.direction_x = 0
              qubert.direction_y = -1*qubert.step_size
          elif event.key == pygame.K_DOWN:
              qubert.direction_x = 0
              qubert.direction_y = 1*qubert.step_size
          elif event.key == pygame.K_LEFT:
              qubert.direction_x = -1*qubert.step_size
              qubert.direction_y = 0
          elif event.key == pygame.K_RIGHT:
              qubert.direction_x = 1*qubert.step_size
              qubert.direction_y = 0
          elif event.key == pygame.K_p:
              paused = True
          elif event.key == pygame.K_q:
              running = False

  pygame.display.flip()

  clock.tick(50)





