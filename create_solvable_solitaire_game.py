from Suit import Suit
from Rank import Rank
from Card import Card
from Deck import Deck
from Solitaire import Solitaire


def create_solvable_solitaire_game():
    cards = [
        Card(Suit.HEART, Rank.ACE),
        Card(Suit.HEART, Rank.THREE),
        Card(Suit.HEART, Rank.TWO),
        Card(Suit.HEART, Rank.SIX),
        Card(Suit.HEART, Rank.FIVE),
        Card(Suit.HEART, Rank.FOUR),
        Card(Suit.HEART, Rank.TEN),
        Card(Suit.HEART, Rank.NINE),
        Card(Suit.HEART, Rank.EIGHT),
        Card(Suit.HEART, Rank.SEVEN),
        Card(Suit.DIAMOND, Rank.TWO),
        Card(Suit.DIAMOND, Rank.ACE),
        Card(Suit.HEART, Rank.KING),
        Card(Suit.HEART, Rank.QUEEN),
        Card(Suit.HEART, Rank.JACK),
        Card(Suit.DIAMOND, Rank.EIGHT),
        Card(Suit.DIAMOND, Rank.SEVEN),
        Card(Suit.DIAMOND, Rank.SIX),
        Card(Suit.DIAMOND, Rank.FIVE),
        Card(Suit.DIAMOND, Rank.FOUR),
        Card(Suit.DIAMOND, Rank.THREE),
        Card(Suit.CLUB, Rank.TWO),
        Card(Suit.CLUB, Rank.ACE),
        Card(Suit.DIAMOND, Rank.KING),
        Card(Suit.DIAMOND, Rank.QUEEN),
        Card(Suit.DIAMOND, Rank.JACK),
        Card(Suit.DIAMOND, Rank.TEN),
        Card(Suit.DIAMOND, Rank.NINE),
        Card(Suit.CLUB, Rank.THREE),
        Card(Suit.CLUB, Rank.FOUR),
        Card(Suit.CLUB, Rank.FIVE),
        Card(Suit.CLUB, Rank.SIX),
        Card(Suit.CLUB, Rank.SEVEN),
        Card(Suit.CLUB, Rank.EIGHT),
        Card(Suit.CLUB, Rank.NINE),
        Card(Suit.CLUB, Rank.TEN),
        Card(Suit.CLUB, Rank.JACK),
        Card(Suit.CLUB, Rank.QUEEN),
        Card(Suit.CLUB, Rank.KING),
        Card(Suit.SPADE, Rank.ACE),
        Card(Suit.SPADE, Rank.TWO),
        Card(Suit.SPADE, Rank.THREE),
        Card(Suit.SPADE, Rank.FOUR),
        Card(Suit.SPADE, Rank.FIVE),
        Card(Suit.SPADE, Rank.SIX),
        Card(Suit.SPADE, Rank.SEVEN),
        Card(Suit.SPADE, Rank.EIGHT),
        Card(Suit.SPADE, Rank.NINE),
        Card(Suit.SPADE, Rank.TEN),
        Card(Suit.SPADE, Rank.JACK),
        Card(Suit.SPADE, Rank.QUEEN),
        Card(Suit.SPADE, Rank.KING),
    ]
    cards.reverse()
    deck = Deck(cards)
    game = Solitaire(deck)
    return game
