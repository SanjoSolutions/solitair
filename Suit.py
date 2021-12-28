from enum import IntEnum


class Suit(IntEnum):
    HEART = 0
    DIAMOND = 1
    CLUB = 2
    SPADE = 3

    @staticmethod
    def parse(string):
        try:
            return next(suit for suit in Suit if str(suit) == string)
        except StopIteration:
            raise ValueError('Unexpected string for suit: "' + string + '"')

    def __str__(self):
        if self == Suit.HEART:
            string = 'h'
        elif self == Suit.DIAMOND:
            string = 'd'
        elif self == Suit.CLUB:
            string = 'c'
        elif self == Suit.SPADE:
            string = 's'
        else:
            raise ValueError('Unexpected enumeration member', self)
        return string

    def __repr__(self):
        return self.__str__()

    def is_black(self):
        return self == Suit.CLUB or self == Suit.SPADE

    def is_red(self):
        return self == Suit.HEART or self == Suit.DIAMOND

