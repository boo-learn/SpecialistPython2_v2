class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_pic = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2663", "Spades": "\u2660"}
        return f"{self.value}{suit_pic.get(self.suit)}"

    def equal_suit(self, other):
        return self.suit == other.suit.name


# Инициализация мастей
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Карты
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

cards = []
for s in suits:
    suit_cards = [Card(value, s) for value in values]
    cards.extend(suit_cards)

print(f"cards[{len(cards)}] {', '.join([card.to_str() for card in cards])}")
