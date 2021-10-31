class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon_suits = {'Hearts': '\u2661', 'Diamonds': '\u2662', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{icon_suits[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

cards = []

for value in values:
    for suit in suits:
        card = Card(value, suit)
        cards.append(card)

cards_str = f'{len(cards)}'
for card in cards:
    cards_str += card.to_str() + ', '

print(cards_str.rstrip(', '))
