"""
Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху.
Снова перемешайте колоду и вытяните еще одну.
Если вторая карта меньше первой, повторите “перемешать + вытянуть”,
до тех пор, пока не вытяните карту больше предыдущей карты.
В качестве результата выведи все вытягиваемые карты в консоль.
"""

import random
class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLABS = "Clubs"

    suits_symbols = {"Diamonds": '\u2666',
                     "Hearts": '\u2665',
                     "Spades": '\u2660',
                     "Clubs": '\u2663'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value}{Card.suits_symbols[self.type]}"
        # print('\u2661', '\u2665')
        # print('\u2662', '\u2666')
        # print('\u2667', '\u2663')
        # print('\u2664', '\u2660')

    def __repr__(self):
        return f"{self.value}{Card.suits_symbols[self.type]}"

    def __gt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.types.index(self.type) > Deck.types.index(other_card.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type


class Deck:
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    types = (Card.HEARTS, Card.DIAMONDS, Card.CLABS, Card.SPADES)
    def __init__(self):
        self.cards = []
        self.index = 0
        for type in Deck.types:
            for value in Deck.values:
                self.cards.append(Card(value, type))

    def __repr__(self):
        string = f"deck[{len(self.cards)}]: "
        string += ", ".join([card.to_str() for card in self.cards])
        return string

    def draw(self, x):
        # Считаем начало списка - верхом колоды
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            card = self.cards[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return card

deck = Deck()
deck.shuffle()

# i = 0
# cards = deck.draw(10)
# card_find = Card("10", Card.DIAMONDS)
# for card in deck:
#     if card == card_find:
#         break
#     i += 1
# print(f"Карта {card_find} найдена на {i} позиции.")

card1 = deck.draw(1)

def shuf():
    deck.shuffle()
    card2 = deck.draw(1)
    return card2

card2 = shuf()
i = 1

while card2 < card1:
    print(f"Операция {i}: карта № 1 {card1} <==> Карта № 2 {card2}")
    if card2 < card1:
        card2 = shuf()
    else:
        break
    i += 1

print(f"Теперь карта № 2 {card2} больше карты № 1 {card1}")
