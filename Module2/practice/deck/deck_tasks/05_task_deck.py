#!/usr/bin
import random

class Card:
    type_to_name = {"Hearts" : '\u2665',
                    "Spades" : '\u2660',
                    "Diamonds" : '\u2666',
                    "Clubs" : '\u2663'}
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

deck = Deck()
deck.shuffle()
print(deck)
first_player = deck.draw(6)
output1 = "Cards of first player: "
for card in first_player:
    output1 += f"{card.to_str()}  "
print(output1)
second_player = deck.draw(6)
output2 = "Cards of second player: "
for card in second_player:
    output2 += f"{card.to_str()}  "
print(output2)
minimum = len(deck.value_list)
for card in first_player:
    ind = card.ret_value_index()
    if ind < minimum:
        minimum = ind
for card in first_player:
    ind = card.ret_value_index()
    if ind == minimum:
        min_card = card
        break
cards_on_the_table = [min_card.value]
print(f"Card of the first player with smallest value: {min_card.to_str()}")
first_player.remove(min_card)
final_winner = False
while True:
    flag = False
    for card in second_player:
        if card.type == min_card.type and card.ret_value_index() > min_card.ret_value_index():
            greater_card = card
            cards_on_the_table.append(greater_card.value)
            print(f"Second player hits: {greater_card.to_str()}")
            flag = True
            break
    if not flag:
        final_winner = True
        print("Second player failed to fight back")
        break
    second_player.remove(greater_card)
    flag = False
    for card in first_player:
        if card.value in cards_on_the_table:
            min_card = card
            cards_on_the_table.append(min_card.value)
            print(f"First player throws: {min_card.to_str()}")
            flag = True
            break
    if not flag:
        break
    first_player.remove(min_card)
if not final_winner:
    print("Second player managed to fight back")

