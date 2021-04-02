import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    suit_symbol = {HEARTS: '\u2665',
                   DIAMONDS: '\u2666',
                   SPADES: '\u2660',
                   CLUBS: '\u2663'}

    def __init__(self, value, type_card):
        self.value = value
        self.type = type_card

    def __repr__(self):
        return f"{self.value}{Card.suit_symbol[self.type]}"

    def __gt__(self, other):
        if Deck.values.index(self.value) == Deck.values.index(other.value):
            return Deck.suits.index(self.type) > Deck.suits.index(other.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other.value)

    def __lt__(self, other):
        if Deck.values.index(self.value) == Deck.values.index(other.value):
            return Deck.suits.index(self.type) < Deck.suits.index(other.type)
        else:
            return Deck.values.index(self.value) < Deck.values.index(other.value)

    def equal_suit(self, card):
        return self.type == card.type


class Deck:
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, num_cards=52):
        if num_cards == 36:
            self.cards = [Card(value, type_card)
                          for type_card in Deck.suits for value in Deck.values[4:]]
        else:
            self.cards = [Card(value, type_card)
                          for type_card in Deck.suits for value in Deck.values]

    def __repr__(self):
        return f'deck[{len(self.cards)}]: {", ".join([str(card) for card in self.cards])}'

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

    def __add__(self, other):
        new_deck = Deck()
        new_deck.cards = self.cards + other.cards
        return new_deck

    def merge(self, other):
        self.cards = self.cards + other.cards
        return self

    def max_suit(self):
        suits = {Card.CLUBS: 0, Card.DIAMONDS: 0,
                 Card.HEARTS: 0, Card.SPADES: 0}
        for i in self:
            suits[i.type] += 1
        return max(suits, key=suits.get)

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)


# Способ 1: через метод merge, аналогичный методу append у списков
deck1 = Deck()
deck2 = Deck()
deck1.merge(deck2)
deck1.shuffle()
deck1.draw(int(len(deck1.cards) / 2))
print(deck1.max_suit())

# Способ 2: через перегрузку метода __add__
new_deck1 = Deck()
new_deck2 = Deck()
big_deck = new_deck1 + new_deck2
big_deck.shuffle()
big_deck.draw(int(len(big_deck.cards) / 2))
print(big_deck.max_suit())
