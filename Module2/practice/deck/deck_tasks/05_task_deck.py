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

class Hand:

    def __init__(self, deck, number=6):
        self.cards = Deck.draw(deck, number)

    def __repr__(self):
        string = f'hand[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def move(self):
        min_card = min(self.cards)
        return self.cards.pop(self.cards.index(min_card))

    def beat(self, move):
        beat_cards = []
        for card in self.cards:
            if card.type == move.type and card > move:
                beat_cards.append(card)
        if beat_cards == []:
            return None
        else:
            min_card = min(beat_cards)
            return self.cards.pop(self.cards.index(min_card))

    def add(self, table):
        add_cards = []
        for card in self.cards:
            for card_t in table:
                if card.value == card_t.value:
                    add_cards.append(card)
        if add_cards == []:
            return None
        else:
            min_card = min(add_cards)
            return self.cards.pop(self.cards.index(min_card))


deck = Deck()
deck.shuffle()
hand1 = Hand(deck)
hand2 = Hand(deck)
print(hand1)
print(hand2)
table = []
move1 = hand1.move()
print(move1, end=' ')
table.append(move1)
while True:
    move2 = hand2.beat(move1)
    if move2 is None:
        print('  Игрок 2 забирает карты')
        break
    print(move2, end=' ')
    table.append(move2)
    move1 = hand1.add(table)
    if move1 is None:
        print('  Карты биты')
        break
    print(move1, end=' ')
    table.append(move1)

