# Сюда отправляем решение первой задачи с колодой
import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        suit = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f'{self.value}{suit[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) > Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __lt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) < Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.value) < Deck.values.index(other_card.value)


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]

    def __init__(self):
        self.cards = []
        self.last_card_index = -1
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        deck_string = f'deck[{len(self.cards)}]: '
        for card in self.cards:
            deck_string += str(card) + ", "
        return deck_string

    def __iter__(self):
        self.last_card_index = -1  # сброс счетчика
        return self

    def __next__(self):
        self.last_card_index += 1
        if self.last_card_index >= len(self.cards):
            raise StopIteration
        return self.cards[self.last_card_index]

    def __getitem__(self, item):
        return self.cards[item]

    def draw(self, x):
        drowned_cards = []
        for _ in range(x):
            drowned_cards.append(self.cards.pop(0))
        return drowned_cards

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card2 > card1:
    print(f"Карта {card2} больше {card1}")
elif card2 < card1:
    print(f"Карта {card2} меньше {card1}")
