import pygame, os, sys
from pygame.locals import *
import json

with open("Cards/test.json") as f:
	imgNames = json.load(f)

class CardModel:
	def __init__(self, x, y, cardName):
		self.x = x
		self.y = y
		self.cardName = cardName
		self.img = "Cards/" + imgNames.get(cardName)
		
class CardController:
	def __init__(self):
		card1 = CardModel(100, 850, 'AS')
		card2 = CardModel(300, 850, '7C')
		self.cards = [card1, card2]

class CardView:
	def __init__(self, cardController):
		self.CardController = cardController
		self.images = []
		for c in self.CardController.cards:
			print(c.img)
			self.images.append(pygame.image.load(c.img))
		
	def render(self, surface):
		count = 0
		for c in self.CardController.cards:
			surface.blit(self.images[count], (c.x, c.y))
			count += 1