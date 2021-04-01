import random


class Card:
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'
    SPADES = 'spades'
    types_symbols = {'hearts': '\u2661',
                     'diamonds': '\u2662',
                     'clubs': '\u2667',
                     'spades': '\u2664'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f'{self.value}{Card.types_symbols[self.type]}'

    def __gt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.types.index(self.type) > Deck.types.index(other_card.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type


class Deck:
    types = ['spades', 'clubs', 'diamonds', 'hearts']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, num_cards=52):
        self.cards = []
        self.index = 0
        if num_cards == 36:
            self.values = Deck.values[4:]
        for t in Deck.types:
            for v in self.values:
                self.cards.append(Card(v, t))

    def __repr__(self):
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def draw_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return card

    def __getitem__(self, index):
        return self.cards[index]


deck1 = Deck()
deck2 = Deck()
deck1.cards.extend(deck2.cards)
deck1.shuffle()
deck1.draw(52)
print(deck1)
max_type_counter = 0
types_dict = {}
for t in Deck.types:
    type_counter = 0
    for card in deck1.cards:
        if card.type == t:
            type_counter += 1
    types_dict[t] = type_counter
for key, value in types_dict.items():
    if value == max(types_dict.values()):
        print(f'{Card.types_symbols[key]}: {value}', end=' ')
