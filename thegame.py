import pygame, os, sys
from pygame.locals import *
from statemanager import *
from cards import *
from deck.dealer import Dealer
from UI import *
from bitmapfont import *

class PlayGameState(GameState):
	def __init__(self, game):
		super().__init__(game)
		pygame.font.init()
		
		self.game = game
		self.renderers = []
		self.dealer = Dealer(3)
		self.playerHands = self.dealer.get_all_player_hands()  # list of list of strings
		self.font = BitmapFont('fasttracker2-style_12x12.png', 12, 12)
		self.font2 = pygame.font.Font(None, 72)
		self.inputTick = 0
		self.evaluation = None
		self.initialise()
		
		self.dummy = 0
		
	def onEnter(self, previousState):
		pygame.mixer.music.stop()
	
	def initialise(self):
		self.card_controller = CardController()
		playerNo = 0
		for hand in self.playerHands:
			self.card_controller.addCards(playerNo, hand)
			playerNo += 1
		card_renderer = CardView(self.card_controller)
		
		self.renderers.append(card_renderer)
	
	def update(self, gameTime):
		# print("PlayGame Updating")
		print(self.game.isClicked)
	
	def draw(self, surface):
		self.font.draw(surface, "Player 1", 100, 1000)
		self.font.draw(surface, "Player 2", 50, 300)
		self.font.draw(surface, "Player 3", 1580, 300)
		
		# self.font2.render(self.dummy, )

		for view in self.renderers:
			view.render(surface)