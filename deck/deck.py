import itertools
import random

class Deck: 
    def __init__(self): 
        self.suits = ['S', 'C', 'H', 'D']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.deck = list(itertools.product(self.suits, self.values))
        random.shuffle(self.deck)
        self.count = 52
    
    def draw(self): 
        card = self.deck.pop()
        self.count = self.count - 1
        #return card[0] + card[1]
        return card

    def draw_advantage_card(self, suit): 
        for i in range(self.count):  
            if self.deck[i][1] == suit: 
                card = self.deck.pop(i)
                self.count = self.count - 1
                #return card[0] + card[1]
                return card
        #no suits left
        self.count = self.count - 1
        return self.draw()
    
    def get_full_deck(self): 
        return [card[0] + card[1] for card in self.deck]