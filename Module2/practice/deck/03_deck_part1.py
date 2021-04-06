import random

class Card:
    SUITS = ['♥', '♦', '♣', '♠']
    VALUES = [str(i) for i in range(2, 11)]
    for char in ['J', 'Q', 'K', 'A']:
        VALUES.append(char)

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{self.suit}'


    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    # def is_more(self, other_card):
    #     global SUITS
    #     if self.value > other_card.value:
    #         out = True
    #     elif self.value == other_card.value:
    #         suit_self = SUITS.index(self.suit)
    #         suit_other = SUITS.index(other_card.suit)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.deck.append(suit + value)

    def __repr__(self):
        return f'deck[{len(self.deck)}]: ' + str(self.deck)

    def draw(self, how_much):
        out = []
        for i in range(how_much):
            out.append(self.deck.pop(0))
        return out

    def shuffle(self):
        random.shuffle(self.deck)

deck1 = Deck()

print(deck1)

print(deck1.draw(5))

deck1.shuffle()
print(deck1.draw(5))
