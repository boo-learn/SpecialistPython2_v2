class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        if self.type == "Hearts":
            tmp = "\u2665"
        elif self.type == "Diamonds":
            tmp = "\u2666"
        elif self.type == "Clubs":
            tmp = "\u2663"
        else:
            tmp = "\u2660"
        return (f'{self.value}{tmp}')


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
