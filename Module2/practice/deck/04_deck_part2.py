import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = [HEARTS, DIAMONDS, CLUBS, SPADES]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f'{self.value}{suit[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if Card.VALUES.index(self.value) > Card.VALUES.index(other_card.value):
            return True
        elif Card.VALUES.index(self.value) == Card.VALUES.index(other_card.value) \
                and Card.SUITS.index(self.suit) > Card.SUITS.index(other_card.suit):
            return True
        return False

    def less(self, other_card):
        if Card.VALUES.index(self.value) < Card.VALUES.index(other_card.value):
            return True
        elif Card.VALUES.index(self.value) == Card.VALUES.index(other_card.value) \
                and Card.SUITS.index(self.suit) < Card.SUITS.index(other_card.suit):
            return True
        return False


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        print(f'deck[{len(self.cards)}]:', *[card.to_str() + "," for card in self.cards])

    def draw(self, x):
        drowned_cards = []
        for _ in range(x):
            drowned_cards.append(self.cards.pop(0))
        return drowned_cards

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
