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

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

hearts_cards = [Card(value, "Hearts") for value in values]
diamonds_cards = [Card(value, "Diamonds") for value in values[::-1]]

hearts_str = [card.to_str() for card in hearts_cards]
diamonds_str = [card.to_str() for card in diamonds_cards]

print(",".join(hearts_str))
print(",".join(diamonds_str))
