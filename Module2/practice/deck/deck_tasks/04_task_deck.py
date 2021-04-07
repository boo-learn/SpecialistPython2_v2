##Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается
##с 6-ки). Перемешайте их. Вытягивайте карты парами - одну из первой колоды,
##вторую из второй. Если карта из первой колоды окажется больше(старше), то
##записываем 1:0 (условно начисляем победное очко первой колоде), если карты
##одинаковые, то не учитываем очко никуда. Выведите итоговый счет, сравнив
##попарно все карты в колодах.

import random


class Card:
    SUITS = ['♥', '♦', '♣', '♠']
    VALUES = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit        

    def __repr__(self):        
        return f'{self.value}{self.suit}'

    def __gt__(self, other):
        if self.value == other.value:
            return Card.SUITS.index(self.suit) < Card.SUITS.index(other.suit)
        else:
            return Card.VALUES.index(self.value) > Card.VALUES.index(other.value)
    def __eq__(self, other):
        return (self.suit == other.suit) & (self.value == other.value)

    def __lt__(self, other):
        return not self.__gt__(other)

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self, list_cards = None):
        self.count = 0
        self.deck = list_cards if list_cards else []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.deck.append(Card(value, suit))

    def __repr__(self):
        return f'deck[{len(self.deck)}]: ' + ', '.join([str(card) for card in self.deck])

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, key):        
        return self.deck[key]

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count >= len(self.deck):
            raise StopIteration
        card = self.deck[self.count]
        self.count += 1        
        return card

    def __add__(self, other):
        return Deck(self.deck + other.deck)

    def draw(self, how_much):
        out = []
        for i in range(how_much):
            try:
                out.append(self.deck.pop(0))
            except IndexError:
                break
        return out

    def shuffle(self):
        random.shuffle(self.deck)


class Deck_36(Deck):
    def __init__(self):
        self.count = 0
        self.deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES[4:]:
                self.deck.append(Card(value, suit))

deck_1 = Deck_36()
deck_1.shuffle()
deck_2 = Deck_36()

deck_2.shuffle()
score = {'deck_1': 0, 'deck_2': 0}
for card_1, card_2 in zip(deck_1, deck_2):
    if card_1 > card_2:
        score['deck_1'] += 1
    elif card_1 < card_2:
        score['deck_2'] += 1    
if score["deck_1"] == score["deck_2"]:
    print('Ничья!')
else:
    winer = max(score.keys(), key=lambda x: score[x])
    print(f'Выйграл {winer} со счетом {score["deck_1"]}:{score["deck_2"]}')


