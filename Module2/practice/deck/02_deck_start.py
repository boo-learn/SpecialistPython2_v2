class Card:
    def __init__(self, value, type):
        self.value_card = value
        self.type_card = type

    def to_str(self):

        lear = {"Diamonds" : '\u2666', "Hearts" : '\u2665', "Spades" : '\u2660', "Clubs" : '\u2663'}

        return self.value_card, lear[self.type_card]


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
