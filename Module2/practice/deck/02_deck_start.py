#!/usr/bin
import random

type_list = ["hearts", "peaks", "diamonds",  "clubs"]
value_list = [str(i) for i in range(2, 11)] +["J", "Q", "K", "A"]
class Card:
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
        return self.type == card.type and self.value > card.value

    def less(self, card):
        return self.type == card.type and self.value < card.value


class Deck:
    def __init__(self):
        self.cards = []
        for value in value_list:
            for type in type_list:
                self.cards.append(Card(value, type))

    def show(self):
        string = "deck[" + str(len(self.cards)) + "]: "
        for card in self.cards:
            string += card.to_str() + ", "
        string = string[:-2]
        print(string)

    def draw(self, x):
        buf = self.cards
        self.cards = self.cards[x:]
        return buf[:x]

    def shuffle(self):
        self.cards = random.shuffle(self.cards)


deck = Deck()
new_deck = deck.draw(4)

