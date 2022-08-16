class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        card_suits = {
            "Diamonds": '\u2666',
            "Hearts": '\u2665',
            "Spades": '\u2663',
            "Clubs": '\u2660'
        }
        return f"{self.value}{card_suits[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

for suit in suits:
    for value in values:
        cards.append(Card(value, suit))

cards_str = [card.to_str() for card in cards]
print(",".join(cards_str))
