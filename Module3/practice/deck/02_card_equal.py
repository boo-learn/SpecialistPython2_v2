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

    def equal_suit(self, other):
        if self.suit.name == other.suit.name:
            return True
        else:
            return False


# Инициализация мастей
hearts = Suit("Hearts", "\u2665")
diamonds = Suit("Diamonds", "\u2666")
clubs = Suit("Clubs", "\u2663")
spades = Suit("Spades", "\u2660")

# Карты
card1 = Card("10", hearts)
card2 = Card("A", spades)

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
