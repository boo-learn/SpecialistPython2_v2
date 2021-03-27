import random as rnd


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
        return f'deck[{len(self.cards)}]: {show[:-2]}'

    def draw(self, x):
        draw = []
        for i in range(x):
            draw.append(self[i])
        return draw

    def shuffle(self):
        old_cards = self.cards
        shuffle = []
        for i in range(len(self.cards)):
            random_card = rnd.randint(0, len(self.cards) - i)
            shuffle.append(old_cards[random_card])
            del old_cards[random_card]
        return shuffle


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
