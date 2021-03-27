class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    suit_simbol = {DIAMONDS: '\u2666',
                   HEARTS: '\u2665',
                   SPADES: '\u2660',
                   CLUBS: '\u2663'}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        return f'{self.value}{Card.suit_simbol[self.suit]}'


class Deck:
    def __init__(self):
        self.cards = []

    def show(self):
        pass

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
