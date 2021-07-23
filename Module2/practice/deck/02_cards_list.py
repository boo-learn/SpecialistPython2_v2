class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit = {'Spades': '\u2660', 'Clubs': '\u2663', 'Diamonds': '\u2666', 'Hearts': '\u2665'}
        return f'{self.value}{suit[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


hearts_cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for value in values:
    card = Card(value, Card.HEARTS)
    hearts_cards.append(card)

diamonds_cards = []
for value in values:
    card = Card(value, Card.DIAMONDS)
    hearts_cards.append(card)

for card in hearts_cards:
    print(f'{card.to_str()}', end=', ')
