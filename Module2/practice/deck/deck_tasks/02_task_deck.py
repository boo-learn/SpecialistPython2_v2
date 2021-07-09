import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    ICONS = {
        "Diamonds": "\u2666",
        "Hearts": "\u2665",
        "Spades": "\u2660",
        "Clubs": "\u2663"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{self.ICONS[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def get_unicode_by_suit(self):
        return f"{self.ICONS[self.suit]}"

    def __gt__(self, other_card):
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = (Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS)
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) > suits.index(other_card.suit)
        else:
            return values.index(self.value) > values.index(other_card.value)

    def __lt__(self, other_card):
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = (Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS)
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) < suits.index(other_card.suit)
        else:
            return values.index(self.value) < values.index(other_card.value)


class Deck:
    def __init__(self, **kwargs):
        self.cards = []
        if not kwargs:
            values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
            suits = (Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES)
            for i in range(len(suits)):
                for j in range(len(values)):
                    self.cards.append(Card(values[j], suits[i]))
        if "seq" in kwargs:
            if type(kwargs['seq']) is Card:
                self.cards.append(kwargs['seq'])
            else:
                for arg in kwargs['seq']:
                    self.cards.append(arg)
        if "from_six" in kwargs and kwargs['from_six'] == True:
            values = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
            suits = (Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES)
            for i in range(len(suits)):
                for j in range(len(values)):
                    self.cards.append(Card(values[j], suits[i]))

    def __str__(self):
        res_str = f"deck[{len(self.cards)}]: "
        for card in self.cards:
            res_str += f"{card}, "
        return res_str[:-2]

    def draw(self, x):
        hand = []
        for _ in range(x):
            hand.append(self.cards.pop(0))
        if len(hand) == 1:
            return hand[0]
        return Deck(seq=hand)

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def __iter__(self):
        return iter(self.cards)

    def get_max_suits(self):
        dict_suits = {}
        for card in self.cards:
            dict_suits.setdefault(card.suit, 0)
            dict_suits[card.suit] += 1
        sorted_suits = sorted(dict_suits.items(), key=lambda item: item[1], reverse=True)
        filtered_suits = list(filter(lambda item: item[1] == sorted_suits[0][1], sorted_suits))
        res_str = ''
        for suit in filtered_suits:
            res_str += f"{Card(None, suit[0]).get_unicode_by_suit()}, "
        return res_str[:-2]

    def sort_by_value(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.cards) - 1):
                if self.cards[i] > self.cards[i + 1]:
                    self.cards[i], self.cards[i + 1] = self.cards[i + 1], self.cards[i]
                    swapped = True
        return Deck(seq=self.cards)

    def remove(self, val):
        self.cards.remove(val)
        Deck(seq=self.cards)

    def append(self, other):
        if type(other) is Card:
            tmp = []
            for el in self.cards:
                tmp.append(el)
            tmp.append(other)
            self.cards = tmp
            Deck(seq=self.cards)
        if type(other) is Deck:
            for card in other.cards:
                self.cards.append(card)
            Deck(seq=self.cards)

            
            
# Task 2
print("Task 2")
deck = Deck()
deck.shuffle()
cards = deck.draw(10)
print(cards.get_max_suits())
print()
