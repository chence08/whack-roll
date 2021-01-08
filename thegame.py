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
		
		self.gameOver = False
		self.game = game
		self.pot = 0
		self.players = [0, 1, 2]
		self.turn = 0
		self.lost = []

		self.font = BitmapFont('fasttracker2-style_12x12.png', 12, 12)
		self.font2 = pygame.font.Font(None, 72)
		# self.timer = 250
		self.dealerImg = pygame.image.load('dealer.png').convert_alpha()
		self.trophyImg = pygame.image.load('trophy.png').convert_alpha()
		self.trophyCoords = [(200, 1000), (150, 300), (1480, 300)]
		self.evalCoords = {0:(100, 1040), 1:(50, 340), 2:(1580, 340)}
		
		self.currPlayer = 2
		self.chipCount = {0:500, 1:500, 2:500}
		self.keyStop = True
		
		self.initialise()
		
	def newRound(self):
		self.initialise()
	
	
	def onEnter(self, previousState):
		pygame.mixer.music.stop()
	
	def initialise(self):
		self.dealer = Dealer(len(self.players))
		self.playerHands = self.dealer.get_all_player_hands()  # list of list of strings
		self.tableCards = self.dealer.get_table_cards()
		self.evaluation = ['', '', '']
		
		self.turnNames = ['Pre-Flop', 'Flop', 'Turn', 'River']
		self.toDeal = True
		self.winner = -1
		
		self.card_controller = CardController()
		count = 0
		for hand in self.playerHands:
			self.card_controller.addCards(self.players[count], hand)
			count += 1
		self.card_renderer = CardView(self.card_controller)
		
	def deal(self):
		if self.turn == 1:
			for i in range(3):
				self.dealer.open_table_card(0)
			self.tableCards = self.dealer.get_table_cards()
			for i in range(3):
				self.card_controller.addCard(i, self.tableCards[i])
		elif self.turn == 2 or self.turn == 3:
			self.dealer.open_table_card(0)
			self.tableCards = self.dealer.get_table_cards()
			self.card_controller.addCard(self.turn+1, self.tableCards[self.turn+1])
		
		self.card_renderer = CardView(self.card_controller)
		self.evaluation = self.dealer.eval_winner()[1]
		
	
	def update(self, gameTime):
		keys = pygame.key.get_pressed()
		if self.gameOver:
		# 	if keys[K_SPACE] and self.keyStop:
		# 		self.__init__
			pass
		else:
			if keys[K_SPACE] and self.keyStop:
				self.currPlayer = (self.currPlayer + 1) % len(self.players)
				self.keyStop = False
			if keys[K_r]:
				self.keyStop = True
				self.toDeal = True
			
			if keys[K_d] and self.toDeal and self.turn <= 3:
				self.turn += 1
				if self.turn >= 1:
					self.deal()
				self.toDeal = False  # keyboard jammer
				
				
			if self.game.isClicked and self.chipCount[self.players[self.currPlayer]] >= 10:
				self.chipCount[self.players[self.currPlayer]] -= 10
				self.pot += 10
				
			# winner check
			if self.turn == 4:
				scores = self.dealer.eval_winner()[0]
				self.winner = [i for i, score in enumerate(scores) if score == min(scores)]
				if len(self.winner) > 1:
					pass  # split the pot
				else:
					self.chipCount[self.players[self.winner[0]]] += self.pot
					self.pot = 0
				
				if 0 in self.chipCount.values():
					self.losers = [i for i, chips in self.chipCount.items() if (chips == 0 and i not in self.lost)]
					for loser in self.losers:
						self.players.remove(loser)
						self.lost.append(loser)
						print(loser)
			
				if len(self.players) > 1:
					self.newRound()
					self.turn = -1
				else:
					self.gameOver = True
			
		
		
	
	def draw(self, surface):
		if self.gameOver:
			self.font.centre(surface, str(self.players[0]), 520)
			self.font.centre(surface, "Press Spacebar to replay!", 560)
		
		else:
			self.font.centre(surface, self.turnNames[self.turn], 48)
			self.font.centre(surface, f"Pot: {self.pot}", 80)
			
			self.font.draw(surface, "Player 1", 100, 1000)
			self.font.draw(surface, str(self.chipCount[0]), 100, 1020)
			# self.font.draw(surface, self.evaluation[0], 100, 1040)
			
			self.font.draw(surface, "Player 2", 50, 300)
			self.font.draw(surface, str(self.chipCount[1]), 50, 320)
			# self.font.draw(surface, self.evaluation[1], 50, 340)
			
			self.font.draw(surface, "Player 3", 1580, 300)
			self.font.draw(surface, str(self.chipCount[2]), 1580, 320)
			# self.font.draw(surface, self.evaluation[2], 1580, 340)
	
			evalCount = 0
			for p in self.players:
				evalx = self.evalCoords[p][0]
				evaly = self.evalCoords[p][1]
				self.font.draw(surface, self.evaluation[evalCount], evalx, evaly)
				evalCount += 1
	
			self.card_renderer.render(surface)
			
			dealx = self.card_controller.playerCoords[self.currPlayer][0]
			dealy = self.card_controller.playerCoords[self.currPlayer][2]
	
			surface.blit(self.dealerImg, (dealx, dealy))
			
			if len(self.players) == 1:
				surface.blit(self.trophyImg, self.trophyCoords[self.players[0]][0], self.trophyCoords[self.players[0]][1])