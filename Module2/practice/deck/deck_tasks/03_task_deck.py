import random


class Card:
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    suits_symbols = {DIAMONDS: '\u2666',
                     SPADES: '\u2663',
                     HEARTS: '\u2665',
                     CLUBS: '\u2663'}

    def __init__(self, value, type):
        self.value = value
        self.type = type
        self.index = 0

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def __repr__(self):
        return f"{self.value} {Card.suits_symbols[self.type]}"

    def __gt__(self, other_card):
        if Deck.cards_list.index(self.value) == Deck.cards_list.index(other_card.value):
            return Deck.suits.index(self.type) > Deck.suits.index(other_card.type)
        else:
            return Deck.cards_list.index(self.value) > Deck.cards_list.index(other_card.value)



class Deck:
    suits = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
    cards_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for card in Deck.cards_list:
                self.cards.append(Card(card, suit))

    def __repr__(self):
        string = f"deck[{len(self.cards)}]: "
        string += ", ".join([str(card) for card in self.cards])
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

    def draw(self, x):
        # Начало списка - верх колоды
        buf = self.cards
        self.cards = self.cards[x:]
        return buf[:x]

    def shuffle(self):
        random.shuffle(self.cards)

deck = Deck()

card_f = Card("10", Card.SPADES)
print(card_f)

i = 1
for card in deck:
    if card == card_f:
        break
    i += 1
print(f"Карта {card_f} найдена на {i} позиции")
