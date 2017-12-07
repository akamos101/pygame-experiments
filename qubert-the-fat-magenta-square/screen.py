

import pygame



#############################################################
# CONSTANTS
#############################################################

# Window dimensions.
WIDTH = 640
HEIGHT = 400


# Background color
BG_COLOR = (100, 255, 100)




#############################################################
# Main Screen class object
#############################################################

def initialize():

  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption('Qubert The Fat Magenta Square')

  return screen


def paint_background(screen):
  screen.fill(BG_COLOR)


# Check to see if coordinate is on the screen; return T/F
def onscreen(screen, x, y):
  retval = True
  if x <= 0 or x >= screen.get_width() or y <= 0 or y >= screen.get_height():
    retval = False
  return retval



