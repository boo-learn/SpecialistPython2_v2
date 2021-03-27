#!/usr/bin
import random

class Card:
    more_list = ["JQ", "QK", "KA"]
    less_list = ["AK", "KQ", "QJ"]
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        if self.type == "hearts":
            return self.value + '\u2665'
        elif self.type == "peaks":
            return self.value + '\u2660'
        elif self.type == "diamonds":
            return self.value + '\u2663'
        elif self.type == "clubs":
            return self.value + '\u2663'

    def equal_suit(self, card):
        return self.type == card.type

    def more(self, card):
        pass

    def less(self, card):
        pass


class Deck:
    type_list = ["hearts", "peaks", "diamonds", "clubs"]
    value_list = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    def __init__(self):
        self.cards = []
        for type in self.type_list:
            for value in self.value_list:
                self.cards.append(Card(value, type))

    def show(self):
        string = "deck[" + str(len(self.cards)) + "]: "
        for card in self.cards:
            string += card.to_str() + ", "
        string = string[:-2]
        print(string)

    def draw(self, x):
        # срез колоды это начало списка
        buf = self.cards
        self.cards = self.cards[x:]
        return buf[:x]

    def shuffle(self):
        random.shuffle(self.cards)

deck = Deck()
deck.shuffle()
cards = deck.draw(10)
counters = {"hearts" : 0, "peaks" : 0, "diamonds" : 0, "clubs" : 0}
for card in cards:
    counters[card.type] += 1
maximum = 0
for key in counters:
    if counters[key] > maximum:
        maximum = counters[key]
for key in counters:
    if counters[key] == maximum:
        print(key)
