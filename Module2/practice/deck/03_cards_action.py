class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        suit = {'Spades': '\u2660', 'Clubs': '\u2663', 'Diamonds': '\u2666', 'Hearts': '\u2665'}
        return f'{self.value}{suit[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
for suit in suits:
    for value in values:
        card = Card(value, suit)
        cards.append(card)

deck_string = f'deck[{len(cards)}]: '
for card in cards:
    deck_string += str(card) + ", "
print(deck_string)
