import pygame, os, sys
from pygame.locals import *

# Import states
from statemanager import *
from menu import MainMenuState
from thegame import PlayGameState


thegame = Game("something", 1920, 1080)
mainMenuState = MainMenuState(thegame)
playGameState = PlayGameState(thegame)
mainMenuState.setPlayState(playGameState)

thegame.run(mainMenuState)