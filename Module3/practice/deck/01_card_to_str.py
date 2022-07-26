class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def to_str(self):
        return f"{self.symbol}{self.name}"


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        return f"{self.value}{self.suit.symbol}"


# Инициализация мастей
hearts = Suit("Hearts", "\u2665")
diamonds = Suit("Diamonds", "\u2666")
clubs = Suit("Clubs", "\u2663")
spades = Suit("Spades", "\u2660")

# Карты
card1 = Card("10", hearts)
card2 = Card("A", diamonds)

print(card1.to_str())
print(card2.to_str())
