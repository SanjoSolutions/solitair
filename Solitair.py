from Deck import Deck
from copy import deepcopy

class Solitair:
    @staticmethod
    def create():
        deck = Deck.create()
        deck.shuffle()
        return Solitair(deck)

    def __init__(self, deck):
        self.moves = []

        self.deck = deck

        self.stock_pile = []

        self.piles = [None] * 7
        for index in range(len(self.piles)):
            self.piles[index] = []

        for index in range(7):
            number_of_cards_in_pile = index + 1
            for card_index in range(number_of_cards_in_pile):
                card = self.deck.draw()
                if card_index == number_of_cards_in_pile - 1:
                    card.face_up()
                else:
                    card.face_down()
                self.piles[index].append(card)

        self.foundation_piles = [None] * 4
        for index in range(len(self.foundation_piles)):
            self.foundation_piles[index] = []

    def draw(self):
        if len(self.deck) == 1:
            cards = self.stock_pile
            self.stock_pile = []
            cards.reverse()
            self.deck = Deck(cards)

        card = self.deck.draw()
        self.stock_pile.append(card)

    def copy(self):
        return deepcopy(self)
