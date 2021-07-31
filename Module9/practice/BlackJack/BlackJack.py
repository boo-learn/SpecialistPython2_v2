import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    suits = [CLUBS, SPADES, DIAMONDS, HEARTS]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card): # >
        if Card.values.index(self.value) == Card.values.index(other_card.value):
            return Card.suits.index(self.suit) > Card.suits.index(other_card.suit)
        else:
            return Card.values.index(self.value) > Card.values.index(other_card.value)

    def __lt__(self, other_card): # <
        if Card.values.index(self.value) == Card.values.index(other_card.value):
            return Card.suits.index(self.suit) < Card.suits.index(other_card.suit)
        else:
            return Card.values.index(self.value) < Card.values.index(other_card.value)

    def get_points(self):
        if self.values.index(self.value) < 9:
            return int(self.value)
        elif self.value in 'JQK':
            return 10
        else:
            return 11


# card1.more(card2)

class Deck:

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        self.last_card_index = -1
        for suit in Card.suits:
            for value in Card.values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        s = f'deck[{len(self.cards)}]:'
        # str(card) --> card.__str__()
        for card in self.cards:
            s = s + str(card) + ","
        return s

    def __iter__(self):
        self.last_card_index = -1
        return self

    def __next__(self):
        self.last_card_index += 1
        if self.last_card_index >= len(self.cards):
            raise StopIteration
        return self.cards[self.last_card_index]

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
