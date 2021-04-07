##Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху.
##Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой,
##повторите “перемешать + вытянуть”, до тех пор, пока не вытяните карту больше
##предыдущей карты. В качестве результата выведи все вытягиваемые карты в консоль.

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
    def __init__(self, list_cards=None):
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


deck = Deck()
deck.shuffle()

card_1 = deck.draw(1)
print(*card_1)
deck.shuffle()
card_2 = deck.draw(1)
print(*card_2)

while card_1 > card_2:
    deck.shuffle()
    card_1 = card_2
    card_2 = deck.draw(1)
    print(*card_2)

