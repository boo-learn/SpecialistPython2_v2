class Card:
    types_symbols = {'hearts': '\u2661',
                     'diamonds': '\u2662',
                     'clubs': '\u2667',
                     'spades': '\u2664'}
    types = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f'{self.value}{Card.types_symbols[self.type]}'

class Deck:
    def __init__(self):
        self.cards = []
        for t in Card.types:
            for v in Card.values:
                self.cards.append(Card(v, t))

    def show(self):
        show = ''
        for card in self.cards:
            show += card.to_str() + ', '
        return show[:-2]
    
deck = Deck()
print(deck.show())
