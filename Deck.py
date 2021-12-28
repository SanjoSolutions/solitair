import random
from Card import Card
from Suit import Suit
from Rank import Rank


class Deck:
    @staticmethod
    def create():
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(suit, rank))
        return Deck(cards)

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return self.__str__()
