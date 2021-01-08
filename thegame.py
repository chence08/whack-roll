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
		self.renderers = []
		self.dealer = Dealer(3)
		self.playerHands = self.dealer.get_all_player_hands()  # list of list of strings
		self.font = BitmapFont('fasttracker2-style_12x12.png', 12, 12)
		self.inputTick = 0
		
		self.evaluation = None
		
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
		keys = pygame.key.get_pressed()
		# if (keys[K_UP] or keys[K_DOWN]) and self.inputTick == 0:
		# 	'''
		# 	The user presses the up and down button to select a menu item.
		# 	To prevent the menu selection from spinning out of control,
		# 	the updates are clamped to four per second (250 milliseconds).
		# 	'''
		# 	self.inputTick = 250
		# 	if keys[K_UP]:
		# 		self.index -= 1
		# 		if self.index < 0:
		# 			self.index = len(self.menuItems) - 1
		# 	elif keys[K_DOWN]:
		# 		self.index += 1
		# 		if self.index == len(self.menuItems):
		# 			self.index = 0
		#
		# elif self.inputTick > 0:
		# 	self.inputTick -= gameTime
		# if self.inputTick < 0:
		# 	self.inputTick = 0
		if keys[K_SPACE]:
			print("AAA")
		
		
		for event in pygame.event.get():
			if event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				print(mousex, mousey)
	
	def draw(self, surface):
		self.font.draw(surface, "Player 1", 100, 1000)
		self.font.draw(surface, "Player 2", 50, 300)
		self.font.draw(surface, "Player 3", 1580, 300)

		for view in self.renderers:
			view.render(surface)