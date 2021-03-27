"""
Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
Вытягивайте карты парами - одну из первой колоды, вторую из второй.
Если карта из первой колоды окажется больше(старше), то записываем 1:0 (условно начисляем победное очко первой колоде), если карты одинаковые, то не учитываем очко никуда.
Выведите итоговый счет, сравнив попарно все карты в колодах.
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
    values_52 = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    values_36 = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
    types = (Card.HEARTS, Card.DIAMONDS, Card.CLABS, Card.SPADES)
    def __init__(self, size_deck):
        self.cards = []
        self.index = 0
        for type in Deck.types:
            if size_deck == 52:
                for value in Deck.values_52:
                    self.cards.append(Card(value, type))
            if size_deck == 36:
                for value in Deck.values_36:
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

    def draw_card(self):
        pass

    def deck_36(self):
        values = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __getitem__(self, index):
        return self.cards[index]

deck1 = Deck(36)
print("deck1:", deck1)

deck2 = Deck(36)
print("deck2:", deck2)

deck1.shuffle()
print("deck1 shuffle:", deck1)
deck2.shuffle()
print("deck2 shuffle:", deck2)


card = deck[5]
print(card)


