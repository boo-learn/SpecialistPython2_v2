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
    
    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_one(self):
        self.shuffle()
        return self.cards.pop(0)


deck1 = Deck(36)
deck1.shuffle()
deck2 = Deck(36)
deck2.shuffle()
num_1 = 0
num_2 = 0
while len(deck1.cards) > 0:
    card1 = deck1.draw_one()
    card2 = deck2.draw_one()
    if card1 > card2:
        num_1 += 1
    elif card1 < card2:
        num_2 += 1

print(f'{num_1}:{num_2}')
