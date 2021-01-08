import pygame, os, sys
from pygame.locals import *
import json

with open("Cards/test.json") as f:
	imgNames = json.load(f)

# (x, y)
playerCoords = [(1000, 1150, 850), (50, 200, 100), (1580 ,1730, 100)]

class CardModel:
	def __init__(self, x, y, cardName):
		self.x = x
		self.y = y
		self.cardName = cardName
		self.img = "Cards/" + imgNames.get(cardName)
		
class CardController:
	def __init__(self):
		self.cards = []
		
	def addCards(self, playerNo, hand):
		coords = playerCoords[playerNo]
		card1 = CardModel(coords[0], coords[2], hand[0])
		card2 = CardModel(coords[1], coords[2], hand[1])
		self.cards.append(card1)
		self.cards.append(card2)

	

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