class Card:
    def __init__(self, value, type_card):
        self.value = value
        self.type = type_card
        self.convert = {'Hearts':'\u2665', 'Diamonds':'\u2666', 'Spades':'\u2660', 'Clubs':'\u2663'}

    def to_str(self):
        return f"{self.value}{self.convert[self.type]}"


class Deck:
    def __init__(self):
        self.cards = []

    def show(self):
        pass

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
