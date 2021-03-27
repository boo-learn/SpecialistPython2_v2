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

    suits_weight = {HEARTS: 4,
                    DIAMONDS: 3,
                    CLUBS: 2,
                    SPADES: 1}

    values_weight = {'2': 2,
                     '3': 3,
                     '4': 4,
                     '5': 5,
                     '6': 6,
                     '7': 7,
                     '8': 8,
                     '9': 9,
                     '10': 10,
                     'J': 11,
                     'Q': 12,
                     'K': 13,
                     'A': 14}

    def __init__(self, value, type_card):
        self.value = value
        self.type = type_card

    def __repr__(self):
        return f"{self.value}{Card.suit_symbol[self.type]}"

    def equal_suit(self, card):
        return self.type == card.type

    def more(self, card):
        return (Card.values_weight[str(self.value)] > card.values_weight[str(card.value)])\
                or (Card.suits_weight[self.type] > card.suits_weight[card.type])

    def less(self, card):
        return (Card.values_weight[str(self.value)] < card.values_weight[str(card.value)])\
                or (Card.suits_weight[self.type] < card.suits_weight[card.type])


class Deck:
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(value, type_card)
                      for type_card in Deck.suits for value in Deck.values]

    def __repr__(self):
        return f'deck[{len(self.cards)}]: {", ".join([str(card) for card in self.cards])}'

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)
    
    def shuffle_and_draw_one(self):
        self.shuffle()
        return self.cards.pop(0)


def comparsion_cards():
    all_draw_cards = []
    card_prev = deck.shuffle_and_draw_one()
    all_draw_cards.append(card_prev)
    for _ in range(len(deck.cards)):
        card_next = deck.shuffle_and_draw_one()
        all_draw_cards.append(card_next)
        if card_next.more(card_prev):
            return all_draw_cards
        else:
            card_prev = card_next

deck = Deck()
print(*comparsion_cards())
