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

    def __gt__(self, other_card):
        if Deck.value_list.index(self.value) == Deck.value_list.index(other_card.value):
            return Deck.type_list.index(self.type) > Deck.type_list.index(other_card.type)
        else:
            return Deck.value_list.index(self.value) > Deck.value_list.index(other_card.value)

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
card1 = deck.draw(1)[0]
print(card1.value, card1.type)
deck.shuffle()
card2 = deck.draw(1)[0]
print(card2.value, card2.type)
while card2 < card1:
    deck.shuffle()
    card1 = deck.draw(1)[0]
    print(card1.value, card1.type)
    if card1 < card2:
        break
    else:
        deck.shuffle()
        card2 = deck.draw(1)[0]
        print(card2.value, card2.type)

