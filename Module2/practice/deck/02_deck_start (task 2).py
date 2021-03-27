"""
Задание-2
Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
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


class Deck:
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    types = (Card.HEARTS, Card.DIAMONDS, Card.CLABS, Card.SPADES)
    def __init__(self):
        self.cards = []
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

deck = Deck()
deck.shuffle()

cards = deck.draw(10)

types = {"Hearts" : 0, "Spades" : 0, "Diamonds" : 0, "Clubs" : 0,}

for card in cards:
    # print(card.type)
    if card.type == "Hearts":
        types["Hearts"] += 1
    if card.type == "Spades":
        types["Spades"] += 1
    if card.type == "Diamonds":
        types["Diamonds"] += 1
    if card.type == "Clubs":
        types["Clubs"] += 1

sorted(types, key=types.get)

# print(types)

list_result = sorted(types, key=types.get)

print(f"Мастей {list_result[3]} больше всего.")

