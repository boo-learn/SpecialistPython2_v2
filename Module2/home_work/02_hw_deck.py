# Закончите все Задания: с колодой карт из файла practice/06_task_with_deck.md

# Закончите все Задания: с колодой карт из файла practice/06_task_with_deck.md
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    ICONS = {
        HEARTS: "♥",
        DIAMONDS: "♦",
        SPADES: "♠",
        CLUBS: "♣"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def to_str(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) > Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) > Deck.VALUES.index(other_card.value)

    def __lt__(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) < Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) < Deck.VALUES.index(other_card.value)


class Deck:
    SUITS = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, cards=[]):
        self.card_index = 0
        if len(cards):
            self.cards = cards
        else:
            self.cards = []
            for value in Deck.VALUES:
                for suit in Deck.SUITS:
                    self.cards.append(Card(value, suit))

    def show(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def __str__(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def draw(self, count):
        cards_in_hand = self.cards[:count]
        self.cards = self.cards[count:]
        return cards_in_hand

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        self.card_index = 0
        return self

    def __next__(self):
        card = self.cards[self.card_index]
        self.card_index += 1
        if self.card_index >= len(self.cards):
            raise StopIteration
        return card

    def __add__(self, other_deck):
        return Deck(self.cards + other_deck.cards)


# Задание-6 “Игра в две колоды”
# Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт.
# Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?


deck1 = Deck()
deck2 = Deck()
deck = deck1 + deck2
deck.shuffle()
list_ = deck.draw(52)

print(deck)

suits = {
    Card.HEARTS: 0,
    Card.DIAMONDS: 0,
    Card.SPADES: 0,
    Card.CLUBS: 0
}
for card in deck:
    if card.suit == Card.HEARTS:
        suits[Card.HEARTS] += 1
    elif card.suit == Card.DIAMONDS:
        suits[Card.DIAMONDS] += 1
    elif card.suit == Card.SPADES:
        suits[Card.SPADES] += 1
    elif card.suit == Card.CLUBS:
        suits[Card.CLUBS] += 1

suits = sorted(suits.items(), reverse=True, key=lambda x: x[1])

print(suits)
