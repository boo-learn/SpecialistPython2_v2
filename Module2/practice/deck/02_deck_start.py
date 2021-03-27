#!/usr/bin

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        string = str(self.value)
        if self.type == "hearts":
            return string + '\u2665'
        elif self.type == "peaks":
            return string + '\u2660'
        elif self.type == "diamonds":
            return string + '\u2663'
        elif self.type == "clubs":
            return string + '\u2663'

    def equal_suit(self, card):
        return self.type == card.type

    def more(self, card):
        return self.type == card.type and self.value > card.value

    def less(self, card):
        return self.type == card.type and self.value < card.value


class Deck:
    def __init__(self):
        self.cards = []
        card = Card(8, "clubs")
        print(card.to_str())

    def show(self):
        pass

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
