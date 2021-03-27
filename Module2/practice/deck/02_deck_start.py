class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    suit_simbol = {HEARTS: '\u2665',
                   DIAMONDS: '\u2666',
                   CLUBS: '\u2663',
                   SPADES: '\u2660'}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        return f'{self.value}{Card.suit_simbol[self.suit]}'


class Deck:
    def __init__(self):
        self.cards = []
        for key in Card.suit_simbol:
            for i in Card.values:
                self.cards.append(Card(i, key))

    def show(self):
        tmp = []
        for i in self.cards:
            tmp.append(Card.to_str(i))
        return f'deck[{len(self.cards)}]: {tmp}'

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
