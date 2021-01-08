import pygame, os, sys
from pygame.locals import *
from statemanager import *
from cards import *
from deck.dealer import Dealer
from UI import *

class PlayGameState(GameState):
	def __init__(self, game):
		super().__init__(game)
		self.renderers = None
		self.dealer = Dealer(3)
		self.playerHands = self.dealer.get_all_player_hands()  # list of list of strings
		
		self.action_manager.add_button("test", (50, 50), (50, 30))
		
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
		
		self.renderers = [card_renderer]
	
	def update(self, gameTime):
		events = pygame.event.get()
		actions = self.action_manager.chk_actions(events)  # check button response
		
		for action in actions:
			if action == 'test':
				print("thegame.py")
	
	def draw(self, surface):
		for view in self.renderers:
			view.render(surface)
			
		self.action_manager.draw_buttons(surface)  # drawing the button