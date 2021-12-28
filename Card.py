from Facing import Facing
from Suit import Suit
from Rank import Rank

class Card:
    @staticmethod
    def parse(suit_and_rank):
        suit = Suit.parse(suit_and_rank[0])
        rank = Rank.parse(suit_and_rank[1])
        return Card(suit, rank)

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.facing = Facing.UP

    def __str__(self):
        return str(self.rank) + str(self.suit)

    def __repr__(self):
        return self.__str__()

    def face_up(self):
        self.facing = Facing.UP

    def face_down(self):
        self.facing = Facing.DOWN

    def is_black(self):
        return self.suit.is_black()

    def is_red(self):
        return self.suit.is_red()
