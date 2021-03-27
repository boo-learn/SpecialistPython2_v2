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

    def more(self, other_card):
        types = {"hearts": 3, "diamonds": 2, "clubs": 1, "spades": 0}
        values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
                    '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
        if self.value == other_card.value:
            return types[self.type] > types[other_card.type]
        else:
            return values[self.value] > values[other_card.value]

class Deck:
    types = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

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

deck = Deck()

card1 = Card("Q", "hearts")
card2 = Card("Q", "clubs")
# card2 = Card("2", "diamonds")
if card1.more(card2):
    print(f'Карта {card1} больше карты {card2}')
else:
    print(f'Карта {card2} больше карты {card1}')
