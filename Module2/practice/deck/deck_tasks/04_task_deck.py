import random

class Card:
    types_symbols = {'hearts': '\u2661',
                     'diamonds': '\u2662',
                     'clubs': '\u2667',
                     'spades': '\u2664'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    # def to_str(self):
    #     return f'{self.value}{Card.types_symbols[self.type]}'

    def __repr__(self):
        return f'{self.value}{Card.types_symbols[self.type]}'

    def __gt__(self, other_card):
        types = {"hearts": 3, "diamonds": 2, "clubs": 1, "spades": 0}
        values = {'6': 4, '7': 5, '8': 6, '9': 7,
                    '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
        if self.value == other_card.value:
            return types[self.type] > types[other_card.type]
        else:
            return values[self.value] > values[other_card.value]

class Deck:
    types = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        for t in Deck.types:
            for v in Deck.values:
                self.cards.append(Card(v, t))

    def show(self):
        # show = ''
        # for card in self.cards:
        #     show += card.to_str() + ', '
        # return f'deck[{len(self.cards)}]: {show[:-2]}'
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def __repr__(self):
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def draw(self, x):
        # # Считаем начало списка верхом колоды
        # buf = self.cards
        # self.cards = self.cards[x:]
        # return buf[:x]
        cards = []
        for _ in range (x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

deck1 = Deck()
deck1.shuffle()
deck2 = Deck()
deck2.shuffle()

print(deck1)
print(deck2)
deck1_counter = 0
deck2_counter = 0
for i in range(len(Deck.types) * len(Deck.values)):
    card1 = deck1.draw(1)[0]
    card2 = deck2.draw(1)[0]
    if card1 > card2:
        deck1_counter += 1
    elif card2 > card1:
        deck2_counter += 1

print(f'{deck1_counter}:{deck2_counter}')
