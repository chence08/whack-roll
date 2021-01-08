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
		# self.timer = 250
		self.evaluation = None
		self.dealerImg = pygame.image.load('dealer.png').convert_alpha()
		self.currPlayer = 0
		self.chipCount = [500, 500, 500]
		self.keyStop = True
		
		self.initialise()
		
		
		
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
		# print(self.game.isClicked)
		keys = pygame.key.get_pressed()
		if keys[K_SPACE] and self.keyStop:
			self.currPlayer = (self.currPlayer + 1) % 3
			self.keyStop = False
		if keys[K_r]:
			self.keyStop = True
			
		if self.game.isClicked and self.chipCount[self.currPlayer] >= 10:
			self.chipCount[self.currPlayer] -= 10
			
		
	
	def draw(self, surface):
		self.font.draw(surface, "Player 1", 100, 1000)
		self.font.draw(surface, str(self.chipCount[0]), 100, 1020)
		
		self.font.draw(surface, "Player 2", 50, 300)
		self.font.draw(surface, str(self.chipCount[1]), 50, 320)
		
		self.font.draw(surface, "Player 3", 1580, 300)
		self.font.draw(surface, str(self.chipCount[2]), 1580, 320)
		
		for view in self.renderers:
			view.render(surface)
		
		dealx = self.card_controller.playerCoords[self.currPlayer][0]
		dealy = self.card_controller.playerCoords[self.currPlayer][2]

		surface.blit(self.dealerImg, (dealx, dealy))