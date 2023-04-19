class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2665", "Spades": "\u2665"}
        return self.value + suit_symbols[self.suit]

    def equal_suit(self, new_card):
        return self.suit == new_card.suit


# Создадим несколько карт
card1 = Card("10", "Hearts")
#card2 = Card("A", "Diamonds")
card2 = Card("A", "Hearts")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
