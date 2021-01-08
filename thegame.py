import pygame, os, sys
from pygame.locals import *
from statemanager import *
from cards import *

class PlayGameState(GameState):
	def __init__(self, game):
		super().__init__(game)
		self.renderers = None
		self.initialise()
		
	def onEnter(self, previousState):
		pass
	
	def initialise(self):
		self.card_controller = CardController()
		card_renderer = CardView(self.card_controller)
		
		self.renderers = [card_renderer]
	
	def update(self, gameTime):
		pass
	
	def draw(self, surface):
		for view in self.renderers:
			view.render(surface)