
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
    value_list = [str(i) for i in range(6, 11)] + ["J", "Q", "K", "A"]
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

deck1 = Deck()
deck2 = Deck()
deck1.shuffle()
deck2.shuffle()
deck1_count = 0
deck2_count = 0
for card1, card2 in zip(deck1.cards, deck2.cards):
    if deck1.value_list.index(card1.value) == deck2.value_list.index(card2.value):
        if deck1.type_list.index(card1.type) > deck2.type_list.index(card2.type):
            deck1_count += 1
        else:
            deck2_count += 1
    elif deck1.value_list.index(card1.value) > deck2.value_list.index(card2.value):
        deck1_count += 1
    else:
        deck2_count += 1
print(f"({deck1_count}, {deck2_count})")
