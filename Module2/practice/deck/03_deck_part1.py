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

    def is_more(self, other_card):
        if self.value > other_card.value:
            out = True
        elif self.value == other_card.value:
            suit_self = Card.SUITS.index(self.suit)
            suit_other = Card.SUITS.index(other_card.suit)
            out = suit_self > suit_other
        else:
            out = False
        return out

    def is_less(self, other_card):
        return not self.is_more(other_card)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.deck.append(Card(value, suit))

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
deck1.shuffle()

card1, card2 = deck1.draw(2)

print(card1.is_more(card2))
print(card1.is_less(card2))
