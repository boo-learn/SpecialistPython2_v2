class Card:
    def __init__(self, value, type):
        pass

    def to_str(self):
        pass


class Deck:
    def __init__(self):
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]
        self.cards = [Card(value, type_card) for type_card in self.suits for value in self.values]

    def show(self):
        return f'deck[{len(self.cards)}]: {", ".join([self.cards[i].to_str() for i in range(len(self.cards))])}'

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
