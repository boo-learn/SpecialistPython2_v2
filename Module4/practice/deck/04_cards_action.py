class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon = None
        if self.suit == "Hearts":
            icon = '\u2665'
        elif self.suit == "Diamonds":
            icon = '\u2666'
        elif self.suit == "Spades":
            icon = '\u2660'
        else:
            icon = '\u2663'
        return f'{self.value}{icon}'

    def equal_suit(self, other_card):

        if self.suit == other_card.suit:
            return True
        return False


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

for value in values:
    for suit in suits:
        cards.append(Card(value, suit))

final_str = f'cards [{len(cards)}]'

for card in cards:
    final_str += card.to_str() + ','
print(final_str)
