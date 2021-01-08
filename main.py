import pygame, os, sys
from pygame.locals import *

# Import states
from statemanager import *
from menu import MainMenuState


thegame = Game("something", 800, 800)
mainMenuState = MainMenuState(thegame)

thegame.run(mainMenuState)