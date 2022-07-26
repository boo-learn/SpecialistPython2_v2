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

# Карты
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

hearts_cards = [Card(value, hearts) for value in values]
diamond_cards = [Card(value, diamonds) for value in values]

print(", ".join([card.to_str() for card in hearts_cards]))
print(", ".join([card.to_str() for card in diamond_cards]))
