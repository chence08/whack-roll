from .deck import Deck
from random import randint
from treys import Card, Evaluator

class Dealer: 
    def __init__(self, players): 
        """Creates dealer object

        :param players: number of players, player index is important
        :type players: int
        """
        self.deck = Deck()
        self.players = players
        self.table = []
        self.initialise_hand()
        self.evalTable = []
        self.eval = Evaluator()

    def initialise_hand(self): 
        self.player_hands = [[self.deck.draw() for j in range(2)] for i in range(self.players)]
        
        self.evalHand = [[Card.new(c[1] + c[0].lower()) for c in hand] for hand in self.player_hands]
        # for hand in self.player_hands: 
        #     h = []
        #     for c in hand: 
        #         print(c)
        #         h.append(Card.new(c[1] + c[0].lower()))
        #     self.evalHand.append(h)

    def clear(self): 
        """Resets hands and table
        """
        self.player_hands = []
        self.evalHand = []
        self.table = []
        self.evalHand = []

    def open_table_card(self, minigame_winner): 
        """Opens new table card and checks hands if >= 3 cards

        :param minigame_winner: index of player who won minigame
        :type minigame_winner: int
        :return: -1 if less than 3 cards opened, tuple(list of scores, list of classes) if >= 3, lower score is better
        :rtype: int or tuple
        """
        hand = self.player_hands[minigame_winner]
        if hand[0][0] == hand[1][0]: 
            card = self.deck.draw_advantage_card(suit=hand[0][0])
        else: 
            card = self.deck.draw_advantage_card(suit=hand[randint(0, 1)][0])
        
        self.table.append(card)
        self.evalTable.append(Card.new(card[1] + card[0].lower()))
        
        if len(self.table) >= 3: 
            return self.eval_winner()
        else: 
            return -1
    
    def eval_winner(self): 
        """Returns current assessment of players' score and classes, lower score is better (1 is royal flush)

        :return: Players' scores and classes
        :rtype: tuple of lists
        """
        player_scores = [self.eval.evaluate(self.evalTable, h) for h in self.evalHand]
        player_classes = [self.eval.class_to_string(self.eval.get_rank_class(s)) for s in player_scores]
        return player_scores, player_classes