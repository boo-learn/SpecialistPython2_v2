#!/usr/bin
import random


class Card:
    type_to_name = {"Hearts": '\u2665',
                    "Spades": '\u2660',
                    "Diamonds": '\u2666',
                    "Clubs": '\u2663'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"{self.type} {self.value}"

    def to_str(self):
        return f"{self.value}{self.type_to_name[self.type]}"

    def equal_suit(self, card):
        return self.type == card.type

    def ret_value_index(self):
        return Deck().value_list.index(self.value)

    def __eq__(self, card):
        return self.type == card.type and self.value == card.value

    def __gt__(self, card):
        type_index1 = Deck().type_list.index(self.type)
        type_index2 = Deck().type_list.index(card.type)
        value_index1 = Deck().value_list.index(self.value)
        value_index2 = Deck().value_list.index(card.value)
        return type_index1 >= type_index2 and value_index1 > value_index2

    def __lt__(self, card):
        type_index1 = Deck().type_list.index(self.type)
        type_index2 = Deck().type_list.index(card.type)
        value_index1 = Deck().value_list.index(self.value)
        value_index2 = Deck().value_list.index(card.value)
        return type_index1 <= type_index2 and value_index1 < value_index2


class Deck:
    type_list = ["Hearts", "Spades", "Diamonds", "Clubs"]
    value_list = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self, num=52):
        self.cards = []
        self.index = 0
        if num == 36:
            self.value_list = self.value_list[4:]
        for type in self.type_list:
            for value in self.value_list:
                self.cards.append(Card(value, type))

    def __repr__(self):
        string = f"deck[{str(len(self.cards))}]: "
        string_list = []
        for card in self.cards:
            string_list.append(f"{card.to_str()}")
        string = f"{string}{', '.join(string_list)}"
        return string

    def __add__(self, other_deck):
        self.cards += other_deck.cards
        return self

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

    def __getitem__(self, item):
        return self.cards[item]

    def draw(self, x):
        # срез колоды это начало списка
        buf = self.cards
        self.cards = self.cards[x:]
        return buf[:x]

    def get_card(self, num):
        return self.cards.pop(num)

    def shuffle(self):
        random.shuffle(self.cards)

deck1 = Deck()
deck2 = Deck()
deck = deck1 + deck2
deck.shuffle()
deck.draw(52)
type_to_value = {"Hearts" : 0,
                 "Spades":  0,
                 "Diamonds": 0,
                 "Clubs" : 0}
for card in deck:
    type_to_value[card.type] += 1
maximum = 0
for key in type_to_value:
    if type_to_value[key] > maximum:
        maximum = type_to_value[key]
for key in type_to_value:
    if type_to_value[key] == maximum:
        print(key)

