class Card:
    HEARST = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    value = {"2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "10": 10,
             "J": 10,
             "Q": 10,
             "K": 10,
             "A": 11,
             }
    suits_symbols = {
        "Diamonds": '\u2666',
        "Hearts": '\u2665',
        "Spades": '\u2660',
        "Clubs": '\u2663',
    }

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value}{Card.suits_symbols[self.type]}"


class Deck:
    def __init__(self):
        self.cards = []

        for suits_symbol in Card.suits_symbols:
            for i in Card.value:
                card = Card(i, suits_symbol)
                self.cards.append(card)

    def show(self):
        pass
    def draw(self, x):
        pass

    def shuffle(self):
        pass

deck = Deck()
print(deck.show())
deck.shuffle()
