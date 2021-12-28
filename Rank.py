from enum import IntEnum

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @staticmethod
    def parse(string):
        try:
            return next(rank for rank in Rank if str(rank) == string)
        except StopIteration:
            raise ValueError('Unexpected string for rank: "' + string + '"')

    def __str__(self):
        if self == Rank.TWO:
            string = '2'
        elif self == Rank.THREE:
            string = '3'
        elif self == Rank.FOUR:
            string = '4'
        elif self == Rank.FIVE:
            string = '5'
        elif self == Rank.SIX:
            string = '6'
        elif self == Rank.SEVEN:
            string = '7'
        elif self == Rank.EIGHT:
            string = '8'
        elif self == Rank.NINE:
            string = '9'
        elif self == Rank.TEN:
            string = 'T'
        elif self == Rank.JACK:
            string = 'J'
        elif self == Rank.QUEEN:
            string = 'Q'
        elif self == Rank.KING:
            string = 'K'
        elif self == Rank.ACE:
            string = 'A'
        else:
            raise ValueError('Unexpected enumeration member', self)
        return string

    def __repr__(self):
        return self.__str__()
